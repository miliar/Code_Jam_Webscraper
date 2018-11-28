#include <fstream>

using namespace std;

int main()
{
    int arr[10];
    long N,i=1;
    int t;

    ifstream fin;
    ofstream fout;
    fin.open("file.in");
    fout.open("out.txt");

    fin>>t;
    while(t--)
    {
        for(int k=0;k<10;k++)
            arr[k]=0;
        fin>>N;
        if(N==0)
            fout<<"Case #"<<(i++)<<": INSOMNIA\n";
        else
        {
            long j=1,Nd,d=0;
            int ct=0;
            while(ct<10)
            {
                Nd=N*j;
                j++;

                while(Nd!=0)
                {
                    d=Nd%10;
                    if(arr[d]==0)
                    {   arr[d]++;
                        ct++;
                    }
                    Nd/=10;

                }


            }
            fout<<"Case #"<<(i++)<<": "<<N*(j-1)<<"\n";
        }

    }



    return 0;
}
