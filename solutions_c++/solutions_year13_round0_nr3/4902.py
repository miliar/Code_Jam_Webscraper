#include <fstream>
#include <iostream>
#include <time.h>
#include <math.h> 
#include <map>

using namespace std;

int is_perfect_square(long long n) {
    if (n < 0)
        return false;
    int root(round(sqrt(n)));
    if( n == root * root)
        return root;
    else
        return 0;
}


bool checkPalindrome(long long num){
    
    long long k = num;
    long long rev = 0;
    int dig;
    while (num > 0)
    {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
    }
    if(rev == k)
       return true;
       
    return false;
}

int main(){
    
    clock_t t;
    int f;
    t = clock();
    
    map<long long,int> map1;
    map<long long,bool> pal;
    int count=0;
    int k;
    for(long long i=1;i<=10000000;i++){
            //cout<< checkPalindrome(i) << " " << checkPalindrome(is_perfect_square(i)) << " "<<endl;
         if( checkPalindrome(i) ){
             pal[i] = true;
             if( k=is_perfect_square(i) )
              {
                if( checkPalindrome(k) )
                {
                 ++count;
                }
              }
            }
         map1[i] = count;
    }
    t = clock() - t;
    
    //printf ("It took me %d clicks (%f seconds).\n",t,((float)t)/CLOCKS_PER_SEC);
    
    int t1;
    ifstream input("input.txt");
    ofstream output("output.txt");
    input>> t1;
    int l = 1;
    int n,m;
    
    bool flag=true;
    while(l<=t1){
        
        input>>m>>n;
        output<<"Case #"<< l<<": ";
        if(n<= 10000000){
             
            int temp = map1.find(n)->second - map1.find(m)->second;
            if(m==1 || map1.find(m-1)->second != map1.find(m)->second){
               temp++;
            }
            output<<temp<<endl;
        }else{
           int temp = 0;
           if(m<10000000){
               temp = map1.find(10000000)->second - map1.find(m)->second;
               if(m == 1 || map1.find(m-1)->second != map1.find(m)->second){
                 temp++;
               }
               m = 10000001;
           }
           
           for( int i=m;i<=n;i++){
               if( checkPalindrome(i) ){
                  if( k=is_perfect_square(i) )
                  {
                     if( checkPalindrome(k) )
                     {
                        ++temp;
                     }
                  }
               }
            }
            output<<temp<<endl;
        }
        l++;
    }
    system("pause");
}
