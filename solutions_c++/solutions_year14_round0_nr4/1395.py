#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
	freopen("D-large.in", "r", stdin);
	//freopen("demo.in", "r", stdin);
 	freopen("Dl0.out", "w", stdout);
    int T,N;
    double in;
    vector<double> in1,in2; 
    cin >> T;
    for(int k=1;k<=T;k++)
    {
    	int out1,out2;
    	out1=0;out2=0;
    	cin >> N;
    	for(int i=0;i<N;i++)
    	{
    		cin >> in;
    		in1.push_back(in);
	    }
	    for(int i=0;i<N;i++)
    	{
    		cin >> in;
    		in2.push_back(in);
	    }
	    sort(in1.begin(),in1.end());
		sort(in2.begin(),in2.end()); 
		//out1
		vector<int>::size_type i,j;
		for(i=0,j=0;i!=in1.size();i++)
		{
			if(in1[i]>in2[j])
			{
				out1++;
				j++;
			}
		}
		for(i=0,j=0;i!=in2.size();i++)
		{
			if(in2[i]>in1[j])
			{
				out2++;
				j++;
			}
		}
    	cout <<"Case #"<<k<<": "<<out1<<" "<<N-out2<<endl;
    	in1.clear();
    	in2.clear();
    }
	return 0;
}
