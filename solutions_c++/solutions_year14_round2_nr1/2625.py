#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

int main () {
	string line;
	int noOfCase;
    
	  
	ifstream myfile ("A-small-attempt0 (1).in");
	if (myfile.is_open())
	{  
		ofstream myfileOut;
		myfileOut.open("output.out");
		getline(myfile,line);
		
		istringstream(line) >> noOfCase;
		
		for(int k=0;k<noOfCase;k++)
		{
            int N;
            getline(myfile,line);
            istringstream(line) >> N;
            
			int no_of_char[100][150]={};
            
            
            string previous_str;
            
            bool early_end=false;
            for (int i=0;i<N;i++)
            {
                string strings;
                getline(myfile,line);
                istringstream(line) >>strings;
                char temp=' ';
                int count=1;
                int index=0;
				string final_str;
                
                for (int j=0;j<strings.length();j++)
                {
                    if (temp==strings[j])
                        count++;
                    else
                    {
						temp=strings[j];
                        final_str=final_str+strings[j];
                        no_of_char[i][index-1]=count;
                        count=1;
                        index++;
                    }
                }
				no_of_char[i][index-1]=count;
                if (i==0)
                    previous_str=final_str;
                if (previous_str!=final_str)
                {
                    myfileOut<<"Case #"<<k+1<<": Fegla Won"<<endl;
                    cout<<"Case #"<<k+1<<": Fegla Won"<<endl;
                    early_end=true;
                    break;
                }
            }
			int total_steps=0;
            if (!early_end)
            {
                
                for(int j=0;j<previous_str.length();j++)
                {
                    vector<int> myvector;
                    for (int i=0;i<N;i++)
                    {
                        myvector.push_back(no_of_char[i][j]);                        
                    }
                    sort(myvector.begin(), myvector.end());
                    int steps=0;
                    if (myvector.begin()!=myvector.end())
                    {
                        
                        if(myvector.size()%2==0)
                        {
                            int step1=0,step2=0;
                            int median1=myvector[myvector.size()/2];
                            for (int p=0;p<myvector.size();p++)
                                step1+=abs(median1-myvector[p]);
                            int median2=myvector[myvector.size()/2-1];
                            for (int p=0;p<myvector.size();p++)
                                step2+=abs(median2-myvector[p]);
                            steps=min(step1,step2);
                        }
                        else
                        {
                            int median=myvector[myvector.size()/2];
                            for (int p=0;p<myvector.size();p++)
                                steps+=abs(median-myvector[p]);
                        }
                    }
                    total_steps+=steps;
                }
				cout<<"Case #"<<k+1<<": "<<total_steps<<endl;
				myfileOut<<"Case #"<<k+1<<": "<<total_steps<<endl;
            }

            
            
        }
		int x;
        cin>>x;

		myfileOut.close();				
		myfile.close();
	}
	else cout << "Unable to open file";
	
	return 0;
}