#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

int main () {
	string line;
	int noOfCase,noOfBox;
    vector<double> NBox,KBox;
	  
	ifstream myfile ("D-large.in");
	if (myfile.is_open())
	{  
		ofstream myfileOut;
		myfileOut.open("output.out");
		getline(myfile,line);
		
		istringstream(line) >> noOfCase;
        
		
		for(int k=0;k<noOfCase;k++)
		{			
            getline(myfile,line);
            istringstream(line) >> noOfBox;
            NBox.resize(noOfBox);
            KBox.resize(noOfBox);
            
            stringstream stream;
            getline(myfile,line);
            
            stream<<line;
            for(int i=0;i<noOfBox;i++)
            {
                stream>>NBox[i];
            }
            stream.clear();
            getline(myfile,line);
            stream<<line;
            for(int i=0;i<noOfBox;i++)
            {
                stream>>KBox[i];
            }
            
            sort(NBox.begin(), NBox.end());
            sort(KBox.begin(), KBox.end());
            int ans1=0;
            int indexK=noOfBox-1;
            for (int i=noOfBox-1;i>=0;i--)
            {
                while (indexK>=0)
                {
                    if(NBox[i]>KBox[indexK])
                    {
                        ans1++;
						indexK--;
                        break;
                    }
                    indexK--;
                }
            }
            
            int ans2=noOfBox;
            indexK=0;
            for (int i=0;i<noOfBox;i++)
            {
                while (indexK<noOfBox)
                {
                    if(NBox[i]<KBox[indexK])
                    {
                        ans2--;
						indexK++;
                        break;
                    }
                    indexK++;
                }
            }
            
            
            cout<<"Case #"<<k+1<<": "<<ans1<<" "<<ans2<<endl;			
            myfileOut<<"Case #"<<k+1<<": "<<ans1<<" "<<ans2<<endl;
        }
		
		myfileOut.close();				
		myfile.close();
	}
	else cout << "Unable to open file";
	
	return 0;
}