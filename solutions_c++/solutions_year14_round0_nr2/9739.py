#include <iostream>
#include <cstdio>
#include <map>
#include <cstdlib>
#include <string>
using namespace std;

std::string string_format(const std::string fmt_str, ...) {
  int final_n, n = fmt_str.size() * 2; /* reserve 2 times as much as the length of the fmt_str */
  std::string str;
  std::unique_ptr<char[]> formatted;
  va_list ap;
  while(1) {
    formatted.reset(new char[n]); /* wrap the plain char array into the unique_ptr */
    strcpy(&formatted[0], fmt_str.c_str());
    va_start(ap, fmt_str);
    final_n = vsnprintf(&formatted[0], n, fmt_str.c_str(), ap);
    va_end(ap);
    if (final_n < 0 || final_n >= n)
      n += abs(final_n - n + 1);
    else
      break;
  }
  return std::string(formatted.get());
}

struct two_double{
  double rate;
  double x;

  bool const operator==(const two_double &o) {
    return x == o.x && rate == o.rate;
  }

};

map<string, double> already_cal;

double max_time;
double best_time(double c, double f, double rate, double x, double cur_time){
  //cout<<"C:"<<c<<" F:"<<f<<" Rata:"<<rate<<" X:"<<x<<" time:"<<cur_time <<endl;
  string key = string_format("%6f %6f", rate, x);
  
  map<string, double>::iterator it = already_cal.find(key);

  if(it!=already_cal.end()){
    return it->second;
  }

  if(x<=c){
    already_cal[key] = x/rate;
    return x/rate;
  }

  if((rate-2)/f*c>x||cur_time>max_time){
    already_cal[key] = x/rate;
    return x/rate;
  }

  already_cal[key] = min(best_time(c, f, rate+f, x, cur_time+c/rate), best_time(c, f, rate, x-c, cur_time+c/rate))+c/rate;
  return already_cal[key];
}

int main(int argc, char *argv[]) {
  int round;
  cin>>round;
  for(int i=0; i<round; i++){
    double c, f, x;
    cin>>c>>f>>x;
    //cout<<c<<f<<x<<endl;
    max_time = x/2;
    already_cal.clear();
    printf("Case %d: %8f\n", i+1, best_time(c, f, 2, x, 0));
  }
  return 0;
}
