#include <fstream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

#define LOOP_LIMIT 200

map<char, bool> foundValues;
int loopCount;

void LoadInputs(ifstream&, int&, std::vector<string>&);
void DumpInput(const std::vector<string>&, int);
void RunTests(const std::vector<string>&, vector<string>&);
void EvaluateNumber(int, int&);

int main(int argc, char *argv[])
{
    bool debug = false;

    if(argc < 2)
    {
	fprintf(stderr, "Specify file\n");
	return 1;
    }
    if(argc == 3)
	debug = true;

    ifstream inputFile(argv[1]);
    if(!inputFile.is_open())
    {
	fprintf(stderr, "Could not open: %s\n", argv[1]);
	return 2;
    }

    std::vector<string> testValues, outputs;
    int caseCount = 0;

    LoadInputs(inputFile, caseCount, testValues);
    if(testValues.empty() || (caseCount == -1) || (caseCount != (int)testValues.size()))
    {
	fprintf(stderr, "Load error\n");
	if(debug)
	    DumpInput(testValues, caseCount);
	return 3;
    }

    if(debug)
	DumpInput(testValues, caseCount);
    else
	RunTests(testValues, outputs);

    for(size_t i=0; i<outputs.size(); i++)
    {
	printf("Case #%d: %s\n", (int)i+1, outputs[i].c_str());
    }

    inputFile.close();
    return 0;
}

void RunTests(const vector<string> &inputs, vector<string> &outputs)
{
    string result;
    bool attached;
    outputs.clear();

    for(size_t i=0; i<inputs.size(); i++)
    {
	result = inputs[i][0];
	attached = false;
	for(size_t j=1; j<inputs[i].length(); j++)
	{
	    //printf("i: %lu, result: %s, input: %c\n", i, result.c_str(), inputs[i][j]);
	    (inputs[i][j] >= result[0]) ? result = inputs[i][j] + result : result += inputs[i][j];
	}
	outputs.push_back(result);
    }
}

void LoadInputs(ifstream &file, int &caseCount, std::vector<string> &values)
{
    string value;
 
    values.clear();
    file >> caseCount;
    while(file >> value)
	values.push_back(value);
}

void DumpInput(const std::vector<string> &vec, int count)
{
    printf("Case Count: %d\nInputs:", count);
    for(size_t i=0; i<vec.size(); i++)
	printf("\t%u: %s\n", (unsigned int)i, vec[i].c_str());
}
