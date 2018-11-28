#include <iostream>

#define PI 3.14

int area(int radius){
        int area = radius*radius;
        return area;
}

int getCircles(int r , int t){
        //std::cout<<"radius : "<<r<<" amount of paint : "<<t<<" millilitres"<<std::endl;
        int radius = r;
        int pleft = t;
        int outer=0,inner=0,counts=0;
        while(1){
                inner = area(radius);
                outer = area(radius+1);
                //std::cout<<"radius : "<<radius<<" amount of paint left : "<<pleft<<std::endl;
                if(outer - inner > pleft){
                        break;
                } else if (outer - inner == pleft){
                        return counts+1;
                } else {
                        pleft = pleft - (outer - inner);
                        counts++;
                        radius += 2;
                }
        }
        return counts;
}

int main(int argc, char **argv){

        int T =0,r=0,t=0;
        std::cin>>T;
        for(int i =0;i<T;i++){
                std::cin>>r>>t;
                std::cout<<"Case #"<<i+1<<": "<<getCircles(r,t)<<std::endl;
        }
}
