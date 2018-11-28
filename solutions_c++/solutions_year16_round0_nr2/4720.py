#include <fstream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

void LoadInputs(ifstream&, int&, std::vector<string>&);
void DumpInput(const std::vector<string>&, int);
void RunTests(const std::vector<string>&, std::vector<int>&);

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

    vector<string> testValues;
    vector<int> outputs;
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
	if(outputs[i] == -1)
	    printf("Case #%d: INSOMNIA\n", (int)i+1);
	else
	    printf("Case #%d: %d\n", (int)i+1, outputs[i]);
    }

    inputFile.close();
    return 0;
}

void RunTests(const vector<string> &inputs, vector<int> &outputs)
{
    outputs = vector<int>(inputs.size(), -1);
    int value = 0;
    size_t pos;
    for(size_t i=0; i<inputs.size(); i++)
    {
	string workingString = inputs[i];
	value = 0;

	while((pos = workingString.find_last_of('-')) != string::npos)
	{
	    for(size_t p=0; p<=pos; p++)
	    {
		if(workingString[p] == '-')
		    workingString[p] = '+';
		else
		    workingString[p] = '-';
	    }

	    value++;
	}

	outputs[i] = value;
    }
}

void LoadInputs(ifstream &file, int &caseCount, vector<string> &values)
{
    string value;
 
    values.clear();
    file >> caseCount;
    while(file >> value)
	values.push_back(value);
}

void DumpInput(const vector<string> &vec, int count)
{
    printf("Case Count: %d\nInputs:", count);
    for(size_t i=0; i<vec.size(); i++)
	printf("\t%u: %s\n", (unsigned int)i, vec[i].c_str());
}
