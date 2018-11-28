
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
ifstream input;
input.open("D-small-attempt0.in");
ofstream output;
output.open("D-output.txt");
int cases, currentCase = 1, K, C, S;
input >> cases;
while (currentCase <= cases){
input >> K >> C >> S;
output << "Case #" << currentCase << ": ";
for (int i = 1; i <= K; i++){
output << i << " ";
}
output << endl;
currentCase++;
}
}