#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
using namespace std;
vector<int>mush;
int N;
int maxdiff;
unsigned long long m()
{
    unsigned long long eaten=0;
    maxdiff=0;
    int diff=0;
    for(int i=0;i<N-1;i++)
    {
        if(mush[i]>mush[i+1])
        {
            diff=mush[i]-mush[i+1];
            maxdiff=max(maxdiff,diff);
            eaten+=diff;
        }
    }
    return eaten;
}
unsigned long long mm()
{
    unsigned long long ret=0;
    for(int i=0;i<N-1;i++)
    {
        if(mush[i]<maxdiff)
        {
            ret+=mush[i];
        }
        else
        {
            ret+=maxdiff;
        }
    }
    return ret;
}

int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>N;
        mush.clear();
        mush.reserve(N);
        int temp;
        for(int n=0;n<N;n++)
        {
            cin>>temp;
            mush.push_back(temp);
        }
        printf("Case #%d: ",t);
        cout<<m()<<" ";
        cout<<mm()<<endl;
    }
}
