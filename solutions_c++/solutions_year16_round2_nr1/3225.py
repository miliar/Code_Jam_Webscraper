#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[]) {
  int TEST_FROM = 0;
  int TEST_TO = 123456789;
  if (argc == 3) {
    sscanf(argv[1], "%d", &TEST_FROM);
    sscanf(argv[2], "%d", &TEST_TO);
  }
  //freopen("small.in", "r", stdin);
  //freopen("small.out", "w", stdout);
  freopen("large.in", "r", stdin);
  freopen("large.out", "w", stdout);

  int tt, l, i, x;
  string s, sorted, ans;

  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {

    //---------------------------------------------------------------------------------------------
    // input data starts
    //---------------------------------------------------------------------------------------------
    cin>>s;
    ans.clear();
    l=s.size();
    sorted=s;


    //---------------------------------------------------------------------------------------------
    // input data ends
    //---------------------------------------------------------------------------------------------
                    if (qq < TEST_FROM || qq > TEST_TO) {
                        continue;
                    }
                    printf("Case #%d: ", qq);
                    fflush(stdout);
    //---------------------------------------------------------------------------------------------
    // solution starts
    //---------------------------------------------------------------------------------------------
        sort(sorted.begin(),sorted.end());
        //cout<<sorted<<endl;
        for(i=0;i<l;i++)
        {
            //cout<<sorted[i]<<endl;
            switch(sorted[i])
            {


        case 'Z':
            ans+='0';
            x=sorted.find('Z');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            x=sorted.find('R');
            sorted.erase(x,1);
            x=sorted.find('O');
            sorted.erase(x,1);
            l=sorted.size();
            i-=4;
            break;
        case 'X':
            ans+='6';
            x=sorted.find('X');
            sorted.erase(x,1);
            x=sorted.find('S');
            sorted.erase(x,1);
            x=sorted.find('I');
            sorted.erase(x,1);
            l=sorted.size();
            i-=3;
            break;
        case 'U':
            ans+='4';
            x=sorted.find('U');
            sorted.erase(x,1);
            x=sorted.find('F');
            sorted.erase(x,1);
            x=sorted.find('O');
            sorted.erase(x,1);
            x=sorted.find('R');
            sorted.erase(x,1);
            l=sorted.size();
            i-=4;
            break;
        case 'W':
            ans+='2';
            x=sorted.find('W');
            sorted.erase(x,1);
            x=sorted.find('T');
            sorted.erase(x,1);
            x=sorted.find('O');
            sorted.erase(x,1);
            l=sorted.size();
            i-=3;
            break;
        case 'G':
            ans+='8';
            x=sorted.find('G');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            x=sorted.find('I');
            sorted.erase(x,1);
            x=sorted.find('H');
            sorted.erase(x,1);
            x=sorted.find('T');
            sorted.erase(x,1);
            l=sorted.size();
            i-=5;
            break;
            }

        }
        //LEVEL 2
        for(i=0;i<l;i++)
        {
            //cout<<sorted[i]<<endl;
            switch(sorted[i])
            {


        case 'F':
            ans+='5';
            x=sorted.find('F');
            sorted.erase(x,1);
            x=sorted.find('I');
            sorted.erase(x,1);
            x=sorted.find('V');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            l=sorted.size();
            i-=4;
            break;
        case 'H':
            ans+='3';
            x=sorted.find('T');
            sorted.erase(x,1);
            x=sorted.find('H');
            sorted.erase(x,1);
            x=sorted.find('R');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            l=sorted.size();
            i-=5;
            break;
        case 'O':
            ans+='1';
            x=sorted.find('O');
            sorted.erase(x,1);
            x=sorted.find('N');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            l=sorted.size();
            i-=3;
            break;
        case 'S':
            ans+='7';
            x=sorted.find('S');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            x=sorted.find('V');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            x=sorted.find('N');
            sorted.erase(x,1);
            l=sorted.size();
            i-=5;
            break;

            }

        }
        //LEVEL 3
        for(i=0;i<l;i++)
        {
            //cout<<sorted[i]<<endl;
            switch(sorted[i])
            {


        case 'N':
            ans+='9';
            x=sorted.find('N');
            sorted.erase(x,1);
            x=sorted.find('I');
            sorted.erase(x,1);
            x=sorted.find('N');
            sorted.erase(x,1);
            x=sorted.find('E');
            sorted.erase(x,1);
            l=sorted.size();
            i-=4;
            break;


            }

        }

        //sorted.erase(remove(sorted.begin(), sorted.end(), 'Z'),sorted.end());
        sort(ans.begin(),ans.end());
        cout<<ans<<endl;
        //cout<<sorted<<endl;





    //---------------------------------------------------------------------------------------------
    // solution ends
    //---------------------------------------------------------------------------------------------

    fflush(stdout);
    fprintf(stderr, "test %d solved, time = %d ms\n", qq, (int)clock());
  }
  return 0;
}
