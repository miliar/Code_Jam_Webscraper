#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream fin  ("in.txt");
	ofstream fout ("out.txt");

	int inSize, maxShy, sum, friends;
	string out, audience;
	stringstream ss;
	fin>>inSize;

    for(int CaseNum = 0; CaseNum<inSize; CaseNum++){
        maxShy = 0;
        friends = 0;
        audience = "";
        fin>>maxShy>>audience;
        int *aud = new int[maxShy+1];
        int *sum = new int[maxShy+2];

        for(int i = 0; i<=maxShy; i++){
            ss<<audience[i];
            ss>>aud[i];
            ss.clear();
        }
        sum[0] = 0;
        for(int i = 1; i<=maxShy+1; i++){
            if(sum[i-1]>=i-1){
                sum[i] = sum[i-1]+aud[i-1];
            }
            else{
                friends = friends +1;
                sum[i] = sum[i-1]+aud[i-1]+1;
            }
        }

        fout<<"Case #"<<CaseNum+1<<": "<<friends<<"\n";


        delete[] aud;
        delete[] sum;
    }

    return 0;
}
