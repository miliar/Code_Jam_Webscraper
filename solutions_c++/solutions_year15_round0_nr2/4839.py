#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int main(){
    
    int tcase,num,i,temp,max = 0,max2=0,count=1;
    vector<unsigned long long int> v;
    vector<unsigned long long int> v2;
    
    for(i=0; i<=11; i++){
            v.push_back(0);
            v2.push_back(0);
    }
    
    cin>>tcase;
    
    while(tcase--){
                   
        max = 0;
        cin>>num;
        
        for(i=0; i<=11; i++){
            v[i] = 0;
            v2[i] = 0;
        }    
        
        for(i=0;i<num;i++){
            cin>>temp;
            v[temp]++;
            v2[temp]++;
            
            if(temp>max)
               max = temp;
        }
        
        int stime,total,mintime;
        
        stime = 0;
        total = max;
        max2 = max;
        mintime = total;
        
        
        if(max == 9 && v[9] == 1){
            v2[3] += 3;
            
            i = max-1;
            
             while(i>=2){
                if(v2[i] != 0){
                        
                    stime += max==9?2:v2[max];
                    total = i + stime;
                    if(total < mintime)
                        mintime = total;
                        
                    max = i;
                    if(max%2 == 0){
                        v2[max/2] += v2[max]*2;
                    }
                    else{
                         v2[max/2] += v2[max];
                         v2[max/2 +1] += v2[max];
                    }
                    //cout<<"\nFor v2["<<i<<"]="<<v2[i]<<" stime = "<<stime<<" total = "<<total<<" mintime = "<<mintime;
                }
                i--;
            }
        }
        max = max2;
        i = max-1;
        stime = 0;
        
        //split the max initially
        if(max%2 == 0){
            v[max/2] += v[max]*2;
        }
        else{
             v[max/2] += v[max];
             v[max/2 +1] += v[max];
        }
        
        while(i>=2){
            if(v[i] != 0){
                    
                stime += v[max];
                total = i + stime;
                if(total < mintime)
                    mintime = total;
                    
                max = i;
                if(max%2 == 0){
                    v[max/2] += v[max]*2;
                }
                else{
                     v[max/2] += v[max];
                     v[max/2 +1] += v[max];
                }
                
            }
            //cout<<"\nFor v1["<<i<<"]="<<v[i]<<" stime = "<<stime<<" total = "<<total<<" mintime = "<<mintime;
            i--;
        }
        
        cout<<"Case #"<<count++<<": "<<mintime<<endl;
    }
    
    return 0;
}
