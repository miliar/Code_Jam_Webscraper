#include <bits/stdc++.h>

using namespace std;

int numGenerated = 0;

vector<string> things;

void generateBin(string thing){
    if(thing.length() == 14){
        if(things.size() == 5000000){
            return;
        }
        things.push_back(thing);
        return;
    }
    if(things.size() == 5000000){
        return;
    }
    generateBin(thing + "0");
    generateBin(thing + "1");
}

bitset<500000000> bs;

vector<int> primes;

void sieve(){
    bs.set();
    for(long long i = 2; i < 1000000; i++){
        if(bs[i] == 0){
            continue;
        }
        primes.push_back(i);
        for(long long j = 1; j*i < 1000000; j++){
            bs[j*i] = 0;
        }
    }
}

int main(int argc, const char * argv[]) {
    
    stdout = fopen("/Inputs/output", "w");
    
    sieve();
    
    generateBin("");
    
    printf("Case 1#:\n");
    
    int numDone = 0;
    int index = 0;
    
    while(numDone != 50){
        string curr = things[index];
        bool fail = false;
        
        string newstr = "1" + things[index] + "1";
        
        for(unsigned int j = 2; j <= 10; j++){
            long long whyy = strtol(newstr.c_str(), NULL, j);
            
            bool divisible = false;
            for(int prime : primes){
                if(prime == whyy){
                    break;
                }
                if(whyy%prime == 0){
                    divisible = true;
                    newstr += " ";
                    newstr += to_string(prime);
                    break;
                }
            }
            
            if(!divisible){
                fail = true;
                break;
            }
        }
        
        if(!fail){
            printf("%s\n", newstr.c_str());
            numDone++;
        }
        index++;
    }
    fclose(stdout);
    
    return 0;
}
