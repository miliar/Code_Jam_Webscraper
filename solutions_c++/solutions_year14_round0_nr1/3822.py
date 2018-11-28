
# include<iostream>


using namespace std;


int main ()
{

int T=0, ans1=0, ans2=0, a[4][4], b[4][4] ;

cin>>T;

for(int cases=0; cases < T; ++cases)
    {

cout<<"Case #"<<cases+1 <<": "   ;
        cin>>ans1;
        for(int i=0; i<4; ++i)
            {
                for(int j=0; j <4 ; ++j)
                    {
                        cin>> a[i][j];
                    }
            }



        cin>>ans2;
        for(int i=0; i<4; ++i)
            {
                for(int j=0; j <4 ; ++j)
                    {
                        cin>> b[i][j];
                    }
            }


 /////////////////   logic on a and   b

  int same=0, countSame=0;


        for(int i=0; i<4; ++i)
            {
                for(int j=0; j<4;++j)
                {
                    if(a[ans1-1][i] == b[ans2-1][j])
                        {
                            ++countSame;same= a[ans1-1][i];
                        }
                }
            }
        ////////////////////////////////// decision   /////////////


if(countSame == 1)  { cout<<same<<"\n"; }
else if (countSame > 1 ) { cout<<"Bad magician!\n"; }
else if ( countSame == 0 ) {  cout<<"Volunteer cheated!\n"; }




    }
}
