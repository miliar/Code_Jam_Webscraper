#include <iostream>
#include <iomanip>

using namespace std;

template<typename T>
void cookie(int icase){
  T c, f, x;
  cin >> c >> f >> x;

  const T frate = T(2.0);

  T t_x_last = x / frate;
  T t_f_last = T(0);
  T t_last = t_x_last + t_f_last;

  int n = 1;
  while(true){
    T t_f_this = t_f_last + c / (frate + (n - 1) * f);
    T t_x_this = x / (frate + f * n);  
    T t_this = t_f_this + t_x_this;

    if(t_this > t_last)
      break;
    else {
      t_last = t_this;
      t_f_last = t_f_this;
      t_x_last = t_x_this;
      n++;
    }
  }
  
  cout << "Case #" << icase << ": " << fixed << setprecision(7) << t_last << endl;
}


int main(){
  int ncase;
  cin >> ncase;

  for(int icase = 0; icase < ncase; ++icase){
    cookie<double>(icase + 1);
  }

  return 0;
}