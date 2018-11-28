#include <bits/stdc++.h>
using namespace std;

bool is_prime [1000006];
vector<int> primes ;
int n , j ;
int cnt = 0 ;



long long check(long long num){

    if(num <= 3) return 0 ;
    for(int i = 0 ; i < primes.size() && primes[i] < num ; i++)
        if(num % primes[i] == 0 )return primes[i];
    return 0;

}




long long get(string  num, int base)
{
    reverse(num.begin(),num.end());
    long long ans = 0 ;
    long long coeff = 1LL;
    for(int i = 0 ; i < num.size() ; i++){
        ans += (long long) (num[i] - '0')  * coeff  *1LL;
        coeff *= base * 1LL;
    }
    //if(base == 2) cout << ans <<endl  ;
    return ans;

}

void generate(string s,int index)
{
    if(cnt == j)return ;
   if(index == n){

          vector<long long> divisor ;
         for(int i = 2 ; i <= 10 ; i++)
         {
             long long val = get(s,i);
             long long d = check(val);
             if(d == 0)
              break;
             else divisor.push_back(d);

        }
        if(divisor.size() == 9)
        {
            cnt++ ;
            cout << s << " ";

            for(int i = 0 ; i < 9 ; i++)
                cout << divisor[i] << " ";

            cout << endl;
        }

       return ;
   }


  if(index < n - 1) generate(s + "0", index + 1);
  generate(s + "1",index + 1);


}

void solve(int tt)
{

    cin >> n >> j;
    cout << "Case #" << tt << ":" << endl ;
    generate("1",1);

}







void precalc(){
 memset(is_prime,1,sizeof(is_prime));
 for(int i = 2 ; i <= 1000000 ; i++)
    if(is_prime[i]){
        primes.push_back(i);
        for(int j = i + i ; j <= 1000000 ; j +=i)
            is_prime[j] = false ;

 }


}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    precalc();
    int t;
    cin>>t;
    for(int tt = 1 ; tt <= t ; tt++)
        solve(tt);

    return 0;
}
