#include<bits/stdc++.h>

using namespace std;


long long conv(long long fmask, int base)
{
    long long ans = 0;
    long long pow =1 ;
    while(fmask)
    {

            ans += pow *( fmask%10);

        fmask=fmask/10;
        pow = pow * base;
    }

    return ans;
}

bool isprime(long long x, long long &div)
{

    div = 0;
    long long s = sqrt(x);
    for(long long i=2;i<=s;i++)
    {
        if(x%i==0)
        {
            div = i;
            break;
        }
    }
    if(!div) return true;
    return false;
}
int check(long long fmask,  vector<long long> & divs)
{

    for(int i=2;i<=10;i++)
    {
            long long x = conv(fmask, i);
            long long div = 0;
            if(isprime(x, div)) return 0;
            divs.push_back(div);
    }
    return 1;
}

long long generatemask(long long seed,long long len)
{
    seed  = seed *2;
    seed ++;
    seed = seed + pow(2ll, len - 1);
    //printf(" seed %6x\n", seed);
 //  cout<<seed<<"seed"<<endl;
    long long msk = 0;
    long long pows =1;
    while(seed)
    {
        msk +=(seed&1)*pows;
        seed/=2;
        pows =pows * 10;

    }

    return msk;

}
int main()
{
    ios_base::sync_with_stdio(0);
	int test;
	ifstream cin ("in.txt");
	ofstream cout("out.txt");
	cin >> test;

	for(int t=1;t<=test;t++)
	{
            int n,j;
            cin >> n >> j;
			cout<<"Case #"<<t<<": "<<'\n';
			int c = 0;
			for(long long mask=0;mask<(1ll<<(n-2));mask++)
            {
               //cout<<mask<<"  mask";
                long long fmask = generatemask( mask, n);
                //cout<<fmask<<endl;
                vector<long  long> msk;
                if(check(fmask, msk))
                {
                        cout<<fmask<<" ";
                        for(int j=0;j<msk.size();j++) cout<<msk[j]<<" ";
                        cout<<endl;
                        c++;
                        if(c == j) break;
                }

            }
	}


 	return 0;
}
