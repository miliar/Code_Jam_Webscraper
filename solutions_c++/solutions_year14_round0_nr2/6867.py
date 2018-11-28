#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main()
{
    std::ifstream wordlist("B-large.in");
    ofstream myfile;
    myfile.open ("out.in");
	std::string word;
	int lineNumber=0;
	int caseNum=0;
	int case1=0;
	double C,F,X,cooki=2;

	while(getline(wordlist, word)){
		//Do operation op ("add" or "del") on num
		//"add" should be done in sorted order
		if(lineNumber==0)
        {
            caseNum = atoi(word.c_str());
            //std::cout<<caseNum<<' '<<'\n';
        }
        else if(lineNumber <=caseNum){
            char *pch = strtok (const_cast<char*>(word.c_str())," ");
                    C=atof(pch);
                    pch = strtok (NULL, " ");
                    F=atof(pch);
                    pch = strtok (NULL, " ");
                    X=atof(pch);
                    int i=0;
                    double time1=0;
                    double time2=0;
                    //cout<<i<<endl;
                    time1=time1 + X/cooki;
                     time2=0;
                        for(int k=0;k<=i;k++)
                        {
                            time2=time2 + C/cooki;
                            cooki=cooki + F;
                        }
                        time2=time2 + X/cooki;
                        cooki=2;
                    for(i=1;time2<=time1;i++)
                    {
                        time1=time2;
                        time2=0;
                        for(int k=0;k<=i;k++)
                        {
                            time2=time2 + C/cooki;
                            cooki=cooki + F;
                        }
                        time2=time2 + X/cooki;
                        cooki=2;
                    }
                    myfile << fixed << showpoint << setprecision(7);
                    myfile <<"Case #"<<lineNumber<<": "<<time1<<endl;

        }
		string op = word.substr(0,3);
        lineNumber++;


		//TODO: Add or Remove elements from list here
	}

    return 0;
}

