#include <stdio.h>




/*void scan(int &i){ char c; 
                  while ((c = getchar()) == '\n' || c == ' ' || c == '\r');
                  i = c - '0';
                 };
*/ 


 
 
int main(){
	freopen("small.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int count,t,longitud,mases,aux;
    char tmp[100];
    int pan[100];
	scanf("%d", &t);
	int y = 1;
	while (t>0){
        for (int i=0; i<100; i++){
            tmp[i]='9';
            pan[i]='2';
        }
        longitud=0;
        scanf("%99s",tmp);
        count = 0;
        for (int i=0; i<100; i++){
            if(tmp[i]=='+'){
                pan[i]=1;
                longitud++;
            }
            if(tmp[i]=='-'){
                pan[i]=0;
                longitud++;
            }
        }
        longitud--;
        while(longitud!=-1){
            while(pan[longitud]==1 && longitud >=0){
                longitud--;
            }
            if (longitud>=0){
                mases=0;
                while(pan[mases]==1){
                    mases++;
                }
                if (mases>0){
                    count ++;
                    for (int x= 0; x<mases; x++){
                        pan[x]=0;
                    }
                }
                int p[longitud];
                int aux=0;
                count ++;
                for (int x = longitud; x >= 0; x--){
                        if (pan[x]==0){
                            p[aux] = 1;
                        }
                        else p[aux] = 0;
                        aux++;
                }
                for (int x= 0; x<=longitud; x++){
                        pan[x]=p[x];
                }
            }
        }
        printf("Case #%d: %d\n", y, count);
        t--;
        y++;
    }
	return 0;
}