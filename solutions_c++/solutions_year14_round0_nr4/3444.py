#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("D-large.in");
    fout.open("output.txt");
    int T,N,k,i,j,c1,c2;
    fin>>T;
    for(k=1;k<=T;k++)
    {
        c1=c2=0;
        fin>>N;
        double Naomi[N],Kent[N];
        for(i=0;i<N;i++)
        fin>>Naomi[i];
        for(i=0;i<N;i++)
        fin>>Kent[i];
        sort(Naomi,Naomi+N);
        sort(Kent,Kent+N);
        i=N-1;
        j=N-1;
        while(i>=0 && j>=0)
        {
            if(Kent[j]<Naomi[i])
            {
                i--;
                c1++;
            }
            j--;
        }
        i=0;
        j=0;
        while(i<N && j<N)
        {
            if(Kent[j]>Naomi[i])
            {
                i++;
                c2++;
            }
            j++;
        }
        c2=N-c2;
        fout<<"Case #"<<k<<": "<<c1<<" "<<c2<<endl;
    }
    return 0;
}
