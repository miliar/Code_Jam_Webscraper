#include <bits/stdc++.h>
using namespace std;
int main()
{
    ifstream in("D-small-attempt0.in");
    streambuf *cinbuff = cin.rdbuf();
    cin.rdbuf(in.rdbuf());

    ofstream out("outD");
    streambuf *coutbuf = cout.rdbuf();
    cout.rdbuf(out.rdbuf());

	long long int T, t, x, r, c;
	char *G="GABRIEL";
	char *R="RICHARD";
	cin>>T;
	for( t=1;t<=T;t++ )
    {
		cin>>x>>r>>c;
		if( r > c )
        {
			r = r+c;
			c = r-c;
			r = r-c;
		}
		switch(x)
		{
		    case 1:
                if( x == 1 )
                {
                    cout<<"Case #"<<t<<": "<<G<<endl;
                }
                break;
            case 2:
                if( r % x == 0 || c % x == 0 )
                {
                    cout<<"Case #"<<t<<": "<<G<<endl;
                }
                else
                {
                    cout<<"Case #"<<t<<": "<<R<<endl;
                }
                break;
            case 3:
                if( r == 1 )
                {
                    cout<<"Case #"<<t<<": "<<R<<endl;
                }
                else if( r == 2 )
                {
                    if( c == 3 )
                    {
                       cout<<"Case #"<<t<<": "<<G<<endl;
                    }
                    else
                    {
                        cout<<"Case #"<<t<<": "<<R<<endl;
                    }
                }
                else if( r == 3 )
                {
                   cout<<"Case #"<<t<<": "<<G<<endl;
                }
                else
                {
                    cout<<"Case #"<<t<<": "<<R<<endl;
                }
                break;
            default:
                if( r < 3 )
                {
                    cout<<"Case #"<<t<<": "<<R<<endl;
                }
                else if( r == 3 )
                {
                    if( c == 3 )
                    {
                        cout<<"Case #"<<t<<": "<<R<<endl;
                    }
                    else
                    {
                        cout<<"Case #"<<t<<": "<<G<<endl;
                    }
                }
                else
                {
                    cout<<"Case #"<<t<<": "<<G<<endl;
                }
        }
    }
	return 0;
}
