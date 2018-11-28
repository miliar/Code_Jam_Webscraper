#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include<sstream>
#include<math.h>
#include<map>

using namespace std;

bool isPrime(long n,vector<int>& td){
    for(long x=2;x*x<n;x++){
        if(n%x==0){
            //std::cout<<"Divident"<<x<<std::endl;
            td.push_back(x);
            return false;
        }
    }
    return true;
}

void toBinary(int n,int base)
{
    //int base =2;
    std::string r;
    while(n!=0) {r=(n%base==0 ?"0":"1")+r; n/=base;}
    std::cout<< r;
}

long getDecimal(long bin, int base){
    long decimal=0, i=0, rem;
    while (bin!=0)
    {
        rem = bin%10;
        bin/=10;
        decimal += rem*pow(base,i);
        ++i;
    }
    return decimal;
}

void getBinary(int n, int base,set<long>& jc){
    //
    /*int len = (int)pow(base,n);*/
    //int limit = (int)pow(base,n-1) + 1;//start from lower half of the truth table 1001
    
    double value;
    std::string binary;
    int N = n-1;
    
    for(int i = 0; i < (int)pow(base,n); ++i) {
        
      for(int y=0;y<n;y++){
            double b = (int)pow(base,N);
            double d = i/b;
            value = (int)d % base;
          
          if((value==0 && N==n-1) ||(value==0 && N==0))
              continue;
          
            binary = binary + std::to_string((int)value);
            //std::cout<<value<<" "<<binary<<" "<<binary.size()<<" "<<N<<std::endl;
          //}
        N--;
        if(N<0){
            N =n-1;
            
            //long dec = getDecimal(std::stoi(binary),base);
            //std::cout<<dec<<std::endl;
            //if(dec>limit){
            //long bin = std::stoi(binary);
            //std::cout<<std::stoi(binary)<<std::endl;
            jc.insert(std::stol(binary));//}

            binary.clear();
        }
      }
                //printf("%u%u%u%u \n", (i/8)%2, (i/4)%2, (i/2)%2, (i%2));
        
        
    
    }
        
        //printf("%u%u%u%u%u%u", i/8%2, i/4%2, i/2%2, i%2);
    //}
}


void getNTD(int num){
    for (int i = 2; i*i <=num ; ++i){
        if (num % i == 0)
            cout << i << endl;
    }
}

int main(int argc, const char * argv[])    {
    
        
    //std::ifstream file("A-small-practice.in-2.txt");
    
    std::ifstream file("sample3.txt");
    //ofstream outputFile;
    
    std::set<long> jc;
    std::vector<int> td;
    std::string str;
    std::set<long>::iterator itr;
    std::vector<int>::iterator itd;
    //std::map<long,set<int>> Map;
    
    std::getline(file,str);
    int T = std::stoi(str);
    
    if(T<1)
        return 0;

    long N,J;
    
    getline(file,str);
    std::stringstream ss(str);
    
    ss >> N >> J;
    
    std::ostringstream sec;
    
    //generate binary
    getBinary(N, 2, jc);
    //std::cout<<jc.size();
    itr = jc.begin();
    //itd = td.begin();
    bool p =0;
    
    for(long i=0;i<J;i++){
        int count = 2;
        td.clear();
        while(count<=10){
            long dec = getDecimal(*itr,count);
            //std::cout<<"DEC "<<dec<<" "<<count<<std::endl;
            p = isPrime(dec,td);
            /*
            sec << *itd;
            std::cout<<*itr<<" "<<*itd<<std::endl;
            str = sec.str() + str;
            */
            //std::cout<<i<<std::endl;
            if(p==1){
                jc.erase(itr);
                td.clear();
                i--;
                break;
            }
            count++;
            
            //itd++;
    }
        if(p!=1){
        std::cout<<"CASE"<<i<<" "<<*itr<<" ";
        for(itd = td.begin();itd!=td.end();itd++)
        {
            std::cout<<*itd<<" ";
        }
        std::cout<<std::endl;
        }
        //Map.insert(std::pair<long,set<int>>(*itr,td));
        itr++;
    }
    
    /*//print
    std::map<long,set<int>>::iterator it;
    for (it=Map.begin(); it!=Map.end(); ++it)
        std::cout << it->first << " => " << &it->second << '\n';
    */
    return 0;
}

