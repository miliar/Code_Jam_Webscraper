#include<iostream.h>
#include<fstream>
#include<sstream>
#include<string>
#include<math.h>
#include<vector>
#include <algorithm>

using namespace std;
int main()
{
	ifstream in("D-large.in");
	ofstream out("output.txt");
	int testcase;
	in>>testcase;
	for(long t=1;t<=testcase;t++)
	{
		vector<float> nomi;
		vector<float> ken;
		vector<float> nomi2;
		vector<float> ken2;
		int NOb;
		in>>NOb;
		float hea;
		for(int i=0;i<NOb;i++)
        {
   			in>>hea;
   			nomi.push_back(hea);
   		}
   		for(int i=0;i<NOb;i++)
        {
   			in>>hea;
   			ken.push_back(hea);
   		}
   		
   		sort(nomi.begin(),nomi.begin()+nomi.size());
   		sort(ken.begin(),ken.begin()+ken.size());
   	   		for(int i=0;i<NOb;i++)
   		{
		   	nomi2.push_back(nomi[i]);
		   	ken2.push_back(ken[i]);
        }
   		
        int nomicounter1=0,nomicounter2=0;
   		for(int i=0;i<NOb;i++)
	    {
	    	if(nomi[0]>ken[0])
		    {
	    	   
   		    	nomi.erase(nomi.begin()+0);
   		    	ken.erase(ken.begin()+0);
  		    	 nomicounter1++;
   		    	
		    }
		    else
		    {
    			nomi.erase(nomi.begin()+0);
    			ken.erase(ken.begin()+ken.size()-1);
    		}
	    }
	    
   		for(int i=0;i<NOb;i++)
	    {
    		
    		if(nomi2[0]<ken2[0])
		    {
   		    	nomi2.erase(nomi2.begin()+0);
   		    	ken2.erase(ken2.begin()+0);
		    }
		    else
		    {
		    	nomicounter2++;
    			nomi2.erase(nomi2.begin()+nomi2.size()-1);
    			ken2.erase(ken2.begin()+0);
    		} 
    	}
    	out<<"Case #"<<t<<": "<<nomicounter1<<" "<<nomicounter2<<endl; 
	}
}