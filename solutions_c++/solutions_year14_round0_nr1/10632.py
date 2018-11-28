#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>

#define fori(i,n) for(int (i)=0; (i) < (n); (i)++)
#define pb push_back

using namespace std;

int main(){
  ifstream in;
  ofstream out;
  vector<int> v, s;
  int t, aux, c, garb;

  in.open("A-small-attempt0.in");
  out.open("output.txt");

  v.resize(4);
  s.resize(4);

  in >> t;
  fori(i, t){
    in >> aux;
    fori(j,4){
      if(aux-1 == j){
        in >> v[0] >> v[1] >> v[2] >> v[3];
      }
      else in >> garb >> garb >> garb >> garb;
    }
    in >> aux;
    fori(j,4){
      if(aux-1 == j)
        in >> s[0] >> s[1] >> s[2] >> s[3];
      else in >> garb >> garb >> garb >> garb;
    }
    aux = 0;
    fori(j, 4){
      fori(k, 4){
        if(v[j] == s[k]){
          aux++;
          c = v[j];
        }
      }
    }
    switch(aux){
      case 0:
        out << "Case #" << i+1 << ": Volunteer cheated!" << endl;
        break;
      case 1:
        out << "Case #" << i+1 << ": " << c << endl;
        break;
      default:
        out << "Case #" << i+1 << ": Bad magician!" << endl;
        break;
    }
  }

}
