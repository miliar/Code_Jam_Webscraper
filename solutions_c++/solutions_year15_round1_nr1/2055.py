#include <iostream>
#include <fstream>
using namespace std;

int inputs[100001];
int diffs[100001];

ifstream fin("mush.in");
ofstream fout("mush.out");

int T;

int main()
{
    fin>>T;
    for(int mycase=0;mycase<T;mycase++)
    {
        int N;
        int prev;
        int result1 = 0;
        int result2 = 0;
        int maxDiff=0;
        fin>>N;
        fin>>prev;
        inputs[0] = prev;
        for(int i=0;i<N-1;i++)
        {
            int temp;
            fin>>temp;
            inputs[i+1] = temp;
            diffs[i] = prev-temp;
            prev = temp;
        }
        for(int i=0;i<N-1;i++)
        {
            if(diffs[i]>0)
            {
                result1+=diffs[i];
                if(diffs[i]>maxDiff)
                {
                    maxDiff = diffs[i];
                }
            }
        }
        cout<<maxDiff<<'\n';
        for(int i=0;i<N-1;i++)
        {
            result2 += min(maxDiff, inputs[i]);
            cout<<"result: "<<result2<<'\n';
            cout<<inputs[i]<<'\n';   
        }
        cout<<'\n';

        fout<<"Case #"<<mycase+1<<": "<<result1<<' '<<result2<<'\n';
        
    }
}

int min(int a, int b)
{
    return a<b?a:b;
}
