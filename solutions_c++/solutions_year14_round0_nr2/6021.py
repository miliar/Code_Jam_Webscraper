#include <iostream>
#include <cstdio>

int main(int argc, char ** argv){
    int n; std::cin >>n;
    
    for (unsigned int i = 0; i < n ; i++) {
        double cost, farm_rate, goal;
        std::cin>>cost>>farm_rate>>goal;
        double rate = 2.0;
        double time = 0.0;
        
        while (true) {
            double next_rate = rate + farm_rate;
            time += cost / rate;
            
            if (goal / next_rate < (goal - cost) / rate) {
                rate = next_rate;
            }else{
                time += (goal - cost) / rate;
                break;
            }
        }
        printf("Case #%d: %f\n",i+1, time);
    }
    return 0;
}