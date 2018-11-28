#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>

using namespace std;

int main()
{
    std::ifstream wordlist("A-small-attempt2.in");
    ofstream myfile;
    myfile.open ("out.in");
	std::string word;
	int lineNumber=0;
	int flag=0;
	int shuffle[2][4];
	int f=1;
	int ans;
	int caseNum=0;
	int case1=0;
	int j=0;
	int common=0;
	int choice;
	while(getline(wordlist, word)){
		//Do operation op ("add" or "del") on num
		//"add" should be done in sorted order
		if(lineNumber==0)
        {
            caseNum = atoi(word.c_str());
            //std::cout<<caseNum<<' '<<'\n';
        }
        else if(lineNumber%5==1)
        {
            choice=atoi(word.c_str());
            f=1;
        }
        else
        {
            if(f==choice)
            {
                char *pch = strtok (const_cast<char*>(word.c_str())," ");
                shuffle[j][0]=atoi(pch);
                  for (int i=1;i<4;i++)
                  {
                    pch = strtok (NULL, " ");
                    shuffle[j][i]=atoi(pch);
                  }
                  j++;
            }
            f++;
        }
        if(j>1)
        {
            case1++;
            if(case1<=caseNum)
            {


                for(int i=0;i<4;i++)
                {
                    cout<<shuffle[0][i]<<"\t";
                    for(int k=0;k<4;k++)
                        {
                            if(shuffle[0][i]==shuffle[1][k])
                                {
                                    ans=shuffle[0][i];
                                    common++;
                                }
                        }
                }
                cout<<endl;
                if(common==1)
                {
                    myfile<<"Case #"<<case1<<": "<<ans<<"\n";
                }
                else if(common>1)
                {
                    myfile<<"Case #"<<case1<<": "<<"Bad magician! \n";
                }
                else
                {
                    myfile<<"Case #"<<case1<<": "<<"Volunteer cheated! \n";
                }
                common=0;
            }
            common=0;
            j=0;
        }
		string op = word.substr(0,3);
        lineNumber++;


		//TODO: Add or Remove elements from list here
	}

    return 0;
}

