#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main ()
{
    int test;
    READ("A-small-attempt6.in");
   WRITE("A-small-attempt6.out");
 //   fstream out;
   // out.open("out.txt");
    scanf("%d", &test);
  //  cin >> test;

    int n = 1;
    while (test != 0 )
    {
        int first;
        int arrfirst[4][4];
        int sec ;
        int arrsec [4][4];

        scanf("%d", &first);
      //  cin >> first;
        for ( int i=0; i<4 ; ++i)
            {
                for (int j=0; j<4;++j)
                    {
                        scanf("%d", &arrfirst[i][j]);

                    //    cin >> arrfirst[i][j];
                    }

            }


                scanf("%d", &sec);
        //cin >> sec;
        for ( int i=0; i<4 ; ++i)
            {
                for (int j=0; j<4;++j)
                    {
                        scanf("%d", &arrsec[i][j]);
                     //   cin >> arrsec[i][j];
                    }
            }


        bool found = false, bad = false;int res ;

        for (int i=0 ; i < 4 ; ++i)
            {
           //     cout << "BOOOOM "  ;
         //       cout <<  arrfirst[first-1][i] << endl;
                for ( int j=0 ; j < 4 ; ++j)
                    {
                        if ( found && arrfirst[first-1][i] == arrsec[sec-1][j] )
                        {
                           // fprintf(stderr, "Case #%d : Bad magician!\n", n);
            /*                cout << arrfirst[first-1][0] << " " << arrfirst[first-1][1] << " "  << arrfirst[first-1][2]
                                 <<  " " << arrfirst[first-1][3] << " sec " << arrsec[sec-1][0] << " " << arrsec[sec-1][1]
                                 << " " << arrsec[sec-1][2] << " "  <<  arrsec[sec-1][3] << endl;
              */            cout << "Case #"<<n << ": Bad magician!\n";
                            bad = true;
                            break;
                        }
                        if (arrfirst[first-1][i] == arrsec[sec-1][j])
                            {
                                found=true;
                                res = arrfirst[first-1][i];
                            }
                        }
                    if ( bad )break;

        }

        if ( found  && !bad)
        {
          /*  cout << arrfirst[first-1][0] << " " << arrfirst[first-1][1] << " "  << arrfirst[first-1][2]
                 <<  " " << arrfirst[first-1][3] << " sec " << arrsec[sec-1][0] << " " << arrsec[sec-1][1]
                 << " " << arrsec[sec-1][2] << " "  <<  arrsec[sec-1][3] << endl;
          *///  fprintf(stderr, "Case #%d : %d\n", n,res);
            cout << "Case #"<<n <<": " << res <<endl;
        }
        if ( !found )
        {
      /*      cout << arrfirst[first-1][0] << " " << arrfirst[first-1][1] << " "  << arrfirst[first-1][2]
                 <<  " " << arrfirst[first-1][3] << " sec " << arrsec[sec-1][0] << " " << arrsec[sec-1][1]
                 << " " << arrsec[sec-1][2] << " "  <<  arrsec[sec-1][3] << endl;
        */   // fprintf(stderr, "Case #%d : Volunteer cheated!\n", n);
            cout << "Case #"<<n << ": Volunteer cheated!\n";
        }

    ++n;
    --test;
    }


//    file.close();


return 0;
}
