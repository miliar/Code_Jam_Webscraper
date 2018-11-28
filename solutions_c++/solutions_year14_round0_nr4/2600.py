#include <stdio.h>
#include <algorithm>
#include <list>
using namespace std;

int main(){
    int T; scanf("%d", &T);

    for (int Tcount = 1; Tcount <= T; Tcount++)
    {
    	int N;double TEMP;
    		scanf("%d",&N);
    	list<double> Naomi,Ken,Naomi2,Ken2;
    	for (int i = 0; i < N; ++i)
    	{
    		scanf("%lf",&TEMP);
            Naomi.push_back(TEMP);
    	}
    	for (int i = 0; i < N; ++i)
    	{
            scanf("%lf",&TEMP);
            Ken.push_back(TEMP);
    	}
        Naomi.sort();
        Ken.sort();
    	//sort(Naomi.begin(),Naomi.end());
    	//sort(Ken.begin(),Ken.end());

        Naomi2=Naomi;
        Ken2=Ken;

        int DWcount=0,Wcount=0;

    while(Naomi.begin()!=Naomi.end())
        if(Naomi.front()>Ken.front()){
            Naomi.pop_front();
            Ken.pop_front();
            DWcount++;
        }else{
            Naomi.pop_front();
            Ken.pop_back();
        }
        Naomi=Naomi2;
        Ken=Ken2;
    while(Naomi.begin()!=Naomi.end())
        if(Naomi.back()> Ken.back()){
            Naomi.pop_back();
            Ken.pop_front();
            Wcount++;
        }else{
            double a=Naomi.back();
            Naomi.pop_back();
            list<double>::iterator it =Ken.end()--;
            while(*it>a && it!=Ken.begin())
                it--;
            Ken.pop_back();
        }
    printf("Case #%d: %d %d\n", Tcount,DWcount,Wcount);
}
    return 0;

}