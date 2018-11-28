#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
    fstream file,file1;
    file.open("input.txt");
    file1.open("output.o");
    int T;
    file>>T;
    int N,M;
    vector<vector<int> >lawn;
    for(int i=0;i<T;++i)
    {
        bool possible=true;
        vector<int>rMax;
        vector<int>cMax;
        file>>N>>M;
        lawn.resize(N);
        rMax.resize(N,100);
        cMax.resize(M,100);
        for(int i=0;i<N;++i)
        {
            lawn[i].resize(M);
            for(int j=0;j<M;++j)
            {
                int h;
                file>>h;
                lawn[i][j]=h;
            }
        }
        int max;
        for(int i=0;i<N;++i)
        {
            max=lawn[i][0];
            for(int j=1;j<M;++j)
            {
                if(lawn[i][j]>max)
                max=lawn[i][j];
            }
            rMax[i]=max;
        }

        for(int j=0;j<M;++j)
        {
            max=lawn[0][j];
            for(int i=1;i<N;++i)
            {
                if(lawn[i][j]>max)
                max=lawn[i][j];
            }
            cMax[j]=max;
        }
        for(int i=0;i<N;++i)
        {
            for(int j=0;j<M;++j)
            {
                if(lawn[i][j]!=rMax[i]&&lawn[i][j]!=cMax[j])
                {
                    possible=false;
                    break;
                }
                if(!possible)
                break;
            }
        }
        if(!possible)
        file1<<"Case #"<<i+1<<": NO"<<endl;
        else
        file1<<"Case #"<<i+1<<": YES"<<endl;
    }
    return 0;
    file.close();
    file1.close();
}
