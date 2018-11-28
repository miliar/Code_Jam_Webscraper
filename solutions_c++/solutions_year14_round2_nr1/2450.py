#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>

using namespace std;
int sum,ii;



int cal(vector <int>  bbb)
{
	int sum=0;
	int n=bbb.size();
	sort(bbb.begin(),bbb.end());
	for (int i=0; i<n;i++)
        sum+=abs(bbb[i]-bbb[n/2]);
	return sum;
}


int main() {
    int a,b,c,n;
    int sum,number;
    cin>>n;
    
    for (int i=0;i<n; i++)
    {
        cin>>number;
        int acc;
        string ss[number];
        string tt[number];
        vector <int> arr[number];
        
        
        for (int j=0;j<number; j++)
        {
          	cin>>ss[j];
          	
            tt[j]=ss[j][0];
            acc=1;
            
            for (int k=1;k<ss[j].size();k++)
                if (ss[j][k]!=ss[j][k-1])
                {
                    tt[j]+=ss[j][k];
                    arr[j].push_back(acc);
                    acc=1;
                }
                else
                {
                    acc++;
                }
            arr[j].push_back(acc);
            
        }
        //return 0;
        bool flag=true;
        for (int j=1;j<number; j++)
            if (tt[j]!=tt[j-1])
                flag=false;
        
        if (!flag)
        {
            cout<<"Case #"<<i+1<<": Fegla Won"<<endl;
            continue;
        }
        else
        {
            int sum=0;
            for (int gg=0;gg < arr[0].size(); gg++ )
            {
                vector<int > tmp;
                for (int hh=0; hh< number; hh++)
                    tmp.push_back(arr[hh][gg]);
                sum+=cal(tmp);
            }
            cout<<"Case #"<<i+1<<": "<<sum<<endl;
        }
    }
	return 0;
}