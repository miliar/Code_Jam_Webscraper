#ifndef CODEJAM_H
#define CODEJAM_H

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

class CodeJam {
protected:
    FILE *_fp;
    vector<string> _input, _output;

public:
    CodeJam(FILE *fp = stdin) : _fp(fp) {
    }
    virtual void parseInput(void) {
	char buf[256];
	int T;
	if (fgets(buf, sizeof(buf), _fp) == NULL) {
	    perror("Parse error");
	    exit(-1);
	}
	T = atoi(buf);
	for (int t = 0; t < T; t++) {
	    if (fgets(buf, sizeof(buf), _fp) == NULL) {
		perror("Parse error");
		exit(-1);
	    }
	    buf[strlen(buf) - 1] = 0;
	    _input.push_back(buf);
	}
    }
    void dumpInput(void) {
	for (int i = 0; i < _input.size(); i++) {
	    printf("[%s]\n", _input[i].c_str());
	}
    }
    void dumpOutput(void) {
	for (int i = 0; i < _output.size(); i++) {
	    printf("Case #%d: %s\n", i + 1, _output[i].c_str());
	}
    }
    void solveAll(void) {
	for (int i = 0; i < _input.size(); i++) {
            solve(_input[i]);
        }
    }
    void output(int count) {
        char buf[256];
        snprintf(buf, sizeof(buf), "%d", count);
        _output.push_back(buf);
    }
    void output(char *buf) {
        _output.push_back(buf);
    }
    virtual void solve(const string input) = 0;
};

#endif // CODEJAM
