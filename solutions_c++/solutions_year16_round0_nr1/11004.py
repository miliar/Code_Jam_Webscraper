#include<iostream>
using namespace std;
int main(){
  int t, s, j, a[10], t1, mod, flag = 0, b[10];
  long int n, i, m, z;
  for(i = 0; i<10; i++){
    a[i] = i;
    b[i]=0;
}
  cin >> t;
  t1 = t;
  while(t>0){
    for(i = 0; i < 10; i++)
      b[i] = 0;
    flag = 0;
    cin >> n;
    if(n == 0){
      cout<<"Case #"<<t1-t+1<<": INSOMNIA"<<endl;
      t--;
      continue;
      }
    for(i = 1; i < 1000000; i++){
      m = i*n;
      z = m;
      while(z != 0){
        mod = z%10;
        for(s = 0; s<10; s++){
          if(a[s] == mod)
            b[s] = -1;
        }
      z /= 10;
      }
      flag = 0;
      for(j = 0; j<10; j++){
        if(b[j] == -1)
          flag++;
      }
      if(flag == 10){
        cout<<"Case #"<<t1-t+1<<": "<<m<<endl;
        t--;
        break;
      }

    }
}
return 0;
}
