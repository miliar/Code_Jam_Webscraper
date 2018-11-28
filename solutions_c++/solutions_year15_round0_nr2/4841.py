#include <iostream>
#include<string>
#include<queue>
#include<algorithm>
#include<fstream>
using namespace std;

int min(int a, int b)
{
    return (a<b)?a:b;
}
int main() 
{
	ifstream input("B-small-attempt0.in");
    ofstream output("B-Small_out.txt");
    priority_queue<int> pq1,pq2,pq3;
    int t,d,i,j,element,n,peak,ans=0;
    input>>t;
    for(j=0;j<t;j++)
    {
        input>>d;
        for(i=0;i<d;i++)
        {
            input>>element;
            pq1.push(element);
            pq2.push(element);
            pq3.push(element);
        }
        int count=0;
        int min1=10009;
        while(pq1.top()>1)
        {
            peak= pq1.top();
            min1=min(min1,count+peak);
            count++;
            n=peak;
			pq1.pop();
            pq1.push(n/2);
            pq1.push(n-(n/2));
        }
        min1=min(min1,count+1);
        //
        
        count=0;
        int min2=10009;
        while(pq2.top()>3)
        {
            peak= pq2.top();
            min2=min(min2,count+peak);
            count++;
            n=peak;
			pq2.pop();
            if(n>3)
            {
            pq2.push(n-3);
            pq2.push(3);
            }
        }
        min1=min(min1,count+3);
        
        //
        
        count=0;
        int min3=10009;
        while(pq3.top()>4)
        {
            peak= pq3.top();
            min3=min(min3,count+peak);
            count++;
            n=peak;
			pq3.pop();
            if(n>4)
            {
            pq3.push(n-4);
            pq3.push(4);
            }
        }
        min3=min(min3,count+4);
        ans=min(min1,min2);
        ans=min(ans,min3);
        output<<"Case #"<<j+1<<": "<<ans<<endl;
    }
    
return 0;
}

