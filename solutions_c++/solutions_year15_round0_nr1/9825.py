#include <iostream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{

    int cases = 0;
    cin >> cases;
    int d = cases;
    int i1, i2;
    string s;
    while(cases) {
      --cases;
        cin >> i1;
        //std::cout << i1 << "\n";
        i1 +=1 ;
        cin >> s;
        vector<int> row(i1);

        for(int i = 0; i < i1; i++)
        {
          char c = s[i];
          row[i] = atoi(&c);
        }

        //for(auto i : row)
        //{
          //cout << i <<"\t";
        //}
        //cout << "\n";


      // logic:
      int standing = 0;
      int need = 0;
      for(int i = 0; i < row.size(); ++i)
      {
        if(row[i] == 0)
          continue;
          if(standing < i){
            need += (i - standing);
            standing += need;
          }

            standing += (row[i]);
      }

      std::cout << "Case #" << d - cases << ": " << need <<"\n";
    }



    return 0;
}


