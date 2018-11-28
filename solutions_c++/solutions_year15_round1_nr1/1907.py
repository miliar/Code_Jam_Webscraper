#include "./definitions.h"

int main(int argc, char* argv[]){
  string filename=argv[1];

  ifstream input;
  input.open(filename);
  if (!input.is_open()){
    throwException("file cannot be opened!");
  }

  string line;
  getline(input, line);
  size_t numberOfTests=stol(line.c_str());

  for (size_t testId=0; testId<numberOfTests; ++testId){
    getline(input, line);
    size_t numberOfLooks=stol(line);
    getline(input, line);

    vector<string> tokens=tokenize(line, " ", TrimStyle::Trim);

    vector<unsigned> numbers;
    for (size_t id=0; id<numberOfLooks; ++id)
      numbers.push_back(stol(tokens[id]));

    size_t min1=0;
    for (size_t id=0; id<numberOfLooks-1; ++id)
      if (numbers[id]>numbers[id+1])
        min1+=numbers[id]-numbers[id+1];

    double maxRate=0;
    for (size_t id=0; id<numberOfLooks-1; ++id)
      if (numbers[id]>numbers[id+1]){
        double rate=numbers[id]-numbers[id+1];
        if (rate>maxRate)
          maxRate=rate;
      }

    size_t min2=0;
    for (size_t id=0; id<numberOfLooks-1; ++id)
      if (numbers[id]<maxRate)
        min2+=numbers[id];
      else
        min2+=maxRate;

    cout<<"Case #"<<testId+1<<": "<<min1<<" "<<min2<<endl;
  }
}
