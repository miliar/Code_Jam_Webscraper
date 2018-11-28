#include<iostream>
#include<fstream>
#define cout fout
#define cin fin


using namespace std;

int main()
{
    ifstream fin("input01.txt");
    ofstream fout("output01.txt");
    int T,n,m,c=0;
    int nums[10];
    cin>>T;
    for (int t=1;t<=T;t++)
    {
        cin>>n;
        for (int i=0;i<10;i++)
            nums[i]=0;

        int i;
        for (i=1;i<100;i++)
        {
            m=i*n;
            c=0;
            while (m)
            {
                nums[m%10]++;
                m/=10;
            }
            for (int i=0;i<10;i++)
                if (nums[i])
                    c++;
            if (c==10)
                break;
        }
        if (c==10)
            cout<<"Case #"<<t<<": "<<i*n<<endl;
        else
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
    }
    cin>>T>>T>>T;
    return 0;
}
