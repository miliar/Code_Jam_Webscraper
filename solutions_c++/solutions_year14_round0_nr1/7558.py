#include <iostream>
#include <fstream> 
using namespace std;

#define FOR_INCR(x,y) for(int x = 0; x < y; x++)
#define cout ofile
#define cin ifile
int main()
{

    int T;
    int first;
    int second;
    int a,b,c,d;
    ofstream ofile;
    ofile.open ("out.txt");
    ifstream ifile ("in.txt");
    int ak[4];
    int ac[4];

    cin >> T;

    FOR_INCR(i,T)
    {

      cin >> first;
  //    cout << "CASE " << i + 1 << endl;
  //  cout << first << endl;
      FOR_INCR(j,4)
      {
        cin >> a >> b >> c >> d;
        if (first == j + 1)
        {
          ak[0] = a;
          ak[1] = b;
          ak[2] = c;
          ak[3] = d;
            //cout << first <<"  " << j + 1 << endl;
        }
//        cout << a << "  " << b <<  "  " << c << "   " << d << endl;

      }
     
   //   cout << " GAP " << endl;

      cin >> second;

    //  cout << second << endl;
      FOR_INCR(j,4)
      {
        cin >> a >> b >> c >> d;
        if (second == j + 1)
        {
          ac[0] = a;
          ac[1] = b;
          ac[2] = c;
          ac[3] = d;

            //cout << second <<"  " << j + 1 << endl; 
        }
//        cout << a << "  " << b <<  "   " << c << "  "<< d << endl;
      }

      int pos = -1;
      int num = 0;
      FOR_INCR(j,4)
        FOR_INCR(k,4)
      {

        if (ak[j] == ac[k])
        { pos++;
          //cout << ac[j] << endl;
          if (pos == 0)
          num = ac[k];
        }
            
      }

      if (pos > 0)
      cout << "Case #"<< i+ 1  <<": Bad magician!" << endl;
      else if (pos == -1)
      cout << "Case #"<< i+ 1  <<": Volunteer cheated!" << endl;
      else
      cout << "Case #"<< i+ 1  <<": " << num << endl;
    }

    return 0;
}
