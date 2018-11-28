#include <fstream>

using namespace std;

short T, ans1, ans2, viz[17];

ifstream in("date.in");
ofstream out("date.out");


void solve(short k){
  in>>ans1;
  short i, j, aux, ans3= 0;
  bool ok = false;
  for (i = 1; i<=16; ++i) viz[i] = 0;
  for (i = 1; i<=4; ++i )
    for (j = 1; j <= 4; ++j)
      {
        in >> aux;
        if (i == ans1)
         viz[aux] ++;
      }
  in>>ans2;
  for( i = 1; i<=4; ++i)
    for(j = 1; j<=4; ++j)
    {
      in >> aux;
      if (i == ans2)
        viz[aux]++;
    }

  for (i = 1; i<=16; ++i){
    if (viz[i]==2 && ans3 == 0 ){
      ans3 = i;
      ok  = true;
    }
      else if (ans3 != 0 && viz[i] == 2) {
        out<<"Case #"<<k<<": Bad magician!\n";
        return;
      }
  }
   if (ok == true){
    out<<"Case #"<<k<<": "<<ans3<<"\n";
   }else
    out<<"Case #"<<k<<": Volunteer cheated!\n";

}

int main(){

  in >> T;
  for (short i = 1 ; i <= T; ++i)
    solve(i);

return 0;
}
