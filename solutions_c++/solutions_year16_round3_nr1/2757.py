#include<cstdio>
#include<queue>
using namespace std;

class room{
public:
    int people,name;
    room(int people , int name){
        this->people = people;
        this->name = name;
    }
};

struct cmd{
    bool operator()(const room &A , const room &B){
        return A.people<B.people;
    }
};


int main()
{
    freopen ( "A-large.in", "r" , stdin );
    freopen ( "A-large.out" , "w" , stdout );
    int allt,nowt=0;
    scanf("%d",&allt);
    while(++nowt <= allt){
        priority_queue < room , vector<room> , cmd> PQ;
        int allroom,allp=0;
        scanf("%d",&allroom);
        //printf("%d\n",allroom);
        for(int i=0;i<allroom;++i){
            int people;
            scanf("%d",&people);
            allp+=people;
            //printf("%c%d\n",i+65,people);
            PQ.push( room(people , i) );
        }

        printf("Case #%d:",nowt);

        while(PQ.top().people > 0){
            //printf("%c",PQ.top().name+65);
            int pfir,psec ,nfir,nsec;
            pfir = PQ.top().people;
            nfir = PQ.top().name;
            PQ.pop();

            psec = PQ.top().people;
            nsec = PQ.top().name;
            PQ.pop();

            //printf("\n%d %c %d %c %d\n",pfir,nfir+65 ,psec,nsec+65,allp);

            pfir--;
            allp--;
            printf(" %c",nfir+65);
            int pthi;
            if(PQ.empty())
                pthi = 0;
            else
                pthi = PQ.top().people;

            if(!pfir && !psec)
                break;
            else if(pfir >= psec && psec <= (allp-1)/2){
                pfir--;
                allp--;
                printf("%c",nfir+65);
            }
            else if(pthi <= (allp-1)/2){
                psec--;
                allp--;
                printf("%c",nsec+65);
            }

            PQ.push(room(pfir,nfir) );
            PQ.push(room(psec,nsec) );

        }
        printf("\n");
    }
    return 0;
}
