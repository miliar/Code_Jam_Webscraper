#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<cstring>

using namespace std;

int main()
{

    string s;
    string sa[4];
    int n,n2,i,j;
    int c1x, c2x, inc, c1d, c2d, c1d1, c2d1;
    int c2y[4];
    int c1y[4];
    int print=0;

    while(cin >> n)
    {
        n2=0;

        while (n2<n)
        {
            for (i=0; i<4; i++)
            {
                cin >>sa[i];
                //cout << "Case "<<"#"<<n2<<": "<<symbol<<" won"<<endl;
                //cout<<"L: "<<i<<" "<< sa[i]<<endl;
            }
            memset(c1y, 0, sizeof(c1y));
            memset(c2y, 0, sizeof(c2y));
            print =0;
            inc = 0;
            c1d=0;
            c2d=0;
            c1d1=0;
            c2d1=0;
            for (i=0; i<4; i++)
            {
                c1x = 0;
                c2x = 0;
                //cout <<"LOL L: "<<i<<" "<<endl;
                for (j=0; j<4; j++)
                {
                    if(sa[i][j]=='X')
                    {
                        c1x++;
                        c1y[j]++;
                    }
                    else if (sa[i][j]=='O')
                    {
                        c2x++;
                        c2y[j]++;
                    }
                    else if (sa[i][j]=='T'){
                        c1x++;
                        c2x++;
                        c1y[j]++;
                        c2y[j]++;
                    }
                    else
                        inc++;
                    if (i==j)
                    {
                        if(sa[i][j]=='X')
                            c1d++;
                        else if (sa[i][j]=='O' )
                            c2d++;
                        else if(sa[i][j]=='T')
                        {
                            c1d++;
                            c2d++;
                        }
                    }
                    if ((3-i)==j)
                    {
                        if(sa[i][j]=='X')
                            c1d1++;
                        else if (sa[i][j]=='O')
                            c2d1++;
                        else if(sa[i][j]=='T')
                        {
                            c1d1++;
                            c2d1++;
                        }
                    }

                    //cout << sa[i][j];
                }

                if (c1x==4 && print ==0)
                {
                    cout << "Case "<<"#"<<n2+1<<": X won"<<endl;
                    print=1;
                    break;
                }
                else if (c2x==4 && print==0)
                {
                    cout << "Case "<<"#"<<n2+1<<": O won"<<endl;
                    print=1;
                    break;
                }
            }
            for (i=0; i<4; i++)
            {
                if (c1y[i]==4 && print==0)
                {
                    cout << "Case "<<"#"<<n2+1<<": X won"<<endl;
                    print=1;
                }
                else if (c2y[i]==4 && print==0)
                {
                    cout << "Case "<<"#"<<n2+1<<": O won"<<endl;
                    print=1;
                }
            }

            if (c1d==4 && print == 0)
            {
                cout << "Case "<<"#"<<n2+1<<": X won"<<endl;
                print=1;
            }
            else if (c2d==4 && print == 0)
            {
                cout << "Case "<<"#"<<n2+1<<": O won"<<endl;
                print=1;
            }
            else if (c1d1==4 && print == 0)
            {
                cout << "Case "<<"#"<<n2+1<<": X won"<<endl;
                print=1;
            }
            else if (c2d1==4 && print == 0)
            {
                cout << "Case "<<"#"<<n2+1<<": O won"<<endl;
                print=1;
            }

            else if (print == 0 && inc !=0)
            {
                cout << "Case "<<"#"<<n2+1<<": Game has not completed"<<endl;
            }
            else if(print == 0 && inc ==0)
                cout << "Case "<<"#"<<n2+1<<": Draw"<<endl;


            //cout << "c1d1: "<<c1d1<<" d2d1: "<<c2d1<<endl;
            n2++;
            //cin>>s;
            //cout<<""<<endl;
        }

    }

    return 0;
}
