/*
Google Code Jam 2016
Round 1B
AUTHOR: Phawin Prongpaophan
*/

#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

char word[2222];
int buck[256];
int ans[99];
int n;

void detectnum(int id,char det,char * tdel)
{
    int m = strlen(tdel);
    ans[id] = buck[det];
    if(ans[id]==0) return;
    //printf("Detect %d on %d\n",ans[id],id);
    for(int i=0;i<m;i++)
    {
        buck[tdel[i]]-=ans[id];
        //printf("Eliminate: %c\n",tdel[i]);
    }
    //printf("---\n");
    return;
}

void each(int tc)
{
    scanf("%s",word);
    n = strlen(word);
    for(int i=0;i<=9;i++) ans[i] = 0;
    for(int i='A';i<='Z';i++) buck[i]=0;
    for(int i=0;i<n;i++) buck[word[i]]++;
    //SHOW
    //for(int i='A';i<='Z';i++) if(buck[i]>0) printf("%c: %d\n",i,buck[i]);
    //Switch Case
    detectnum(0,'Z',"ZERO");
    detectnum(6,'X',"SIX");
    detectnum(2,'W',"TWO");
    detectnum(4,'U',"FOUR");
    detectnum(8,'G',"EIGHT");
    detectnum(5,'F',"FIVE");
    detectnum(3,'R',"THREE");
    detectnum(1,'O',"ONE");
    detectnum(7,'V',"SEVEN");
    detectnum(9,'I',"NINE");
    printf("Case #%d: ",tc);
    for(int i=0;i<=9;i++)
    {
        for(int j=0;j<ans[i];j++) printf("%c",i+'0');
    }
    printf("\n");
    return;
}

int main()
{
    freopen("DigitIn.in","r",stdin);
    freopen("DigitOut.txt","w",stdout);

    int tcc; scanf("%d",&tcc);
    for(int tcnt=1;tcnt<=tcc;tcnt++)    each(tcnt);
    return 0;
}
