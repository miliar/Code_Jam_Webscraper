'use strict';
const expect = require('chai').expect; // NOTE: Needs to be installed.
const fs = require('fs');

// Path to executable
const EXECUTABLE = './bin/Debug/A';

// Input files.
const sample0In = fs.readFileSync('sample.0.in', 'utf8');
const sample0Out = fs.readFileSync('sample.0.out', 'utf8');

describe('A', () => {
	it('sample', (done) => {
		doSimpleTest(sample0In, sample0Out, done);
	});
	
	[
		[0, 'INSOMNIA'],
		[100, 900],
		[200, '9000'],
		[1000000, 9000000]
	].forEach((tc) => {
		it(`N=${tc[0]}`, (done) => {
			doSimpleTest(`1\n${tc[0]}\n`, `Case #1: ${tc[1]}\n`, done);
		});
	});
});

function doSimpleTest(input, expectedOutput, done) {
  execute(input, (code, output) => {
		expect(code).to.equal(0);
		expect(output).to.equal(expectedOutput);
		done();
	});
}

function execute(input, onFinished) {
	const spawn = require('child_process').spawn;
	
	const app = spawn(EXECUTABLE, []);
	
	app.stdin.write(input);
// 	app.stdin.close();
	
	let output = '';
	
	app.stdout.on('data', (data) => {
		output += data;
	});
	
	app.stderr.on('data', (data) => {
		output += data;
	});
	
	app.on('close', (code) => {
		onFinished(code, output);
	});
}