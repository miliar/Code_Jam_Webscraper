#include <bits/stdc++.h>

using namespace std;

template <size_t N>
bool increase(bitset<N>& bs)
{
    for (size_t i = 0; i != bs.size(); ++i)
    {
        if (bs.flip(i).test(i) == true)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);

    int t , z = 0 ;
    cin >> t ;
    while( t--)
    {
        int n , j ;
        cin >> n >> j ;

        bitset <8> bs;
        vector < bitset <8> > v;

        do
        {
            v.push_back(bs);
        }
        while (increase(bs));

        long long arr[ v.size() ][11] ;

        for(int i=0 ; i<v.size() ; i++)
        {
            for(int j=2 ; j<=10 ; j++)
            {
                long long sum = 1 , n = j ;
                for(int k=0 ; k<14 ; k++)
                {
                    if( k<8 ) sum += v[i][k]*n;
                    n *= j ;
                }
                sum += n ;

                arr[i][j] = sum ;
            }
        }

        int cnt = 0 ;
        vector <int> vec;

        cout << "Case #" << ++z << ":\n";

        for(int i=0 ; i<v.size() ; i++)
        {
            for(int j=2 ; j<=10 ; j++)
            {
                for(int k=2 ; k<200 ; k++)
                {
                    if( arr[i][j] != k && arr[i][j] % k == 0 )
                    {
                        vec.push_back(k);
                        break ;
                    }
                }
            }

            if( vec.size() == 9 )
            {
                cnt++;
                cout << "1000000" << v[i] << "1 ";
                for(int k=0 ; k<9 ; k++)
                {
                    cout << vec[k] ;
                    if( k < 8 ) cout << " ";
                    else cout << endl;
                }
            }

            vec.clear();
            if( cnt == j ) break ;
        }
    }

}
