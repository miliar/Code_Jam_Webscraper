#include<cstdio>
#include<algorithm> 

int main(void)
{
	int numbersOfCases;
	scanf("%d",&numbersOfCases);
	
	for(int nowCase=1;nowCase<=numbersOfCases;++nowCase){
		
		int numbersOfBlocks;
		double NaomiWeight[2000];
		double KenWeight[2000];
		int answer;
		int NaomiPointer,KenPointer;
		
		scanf("%d",&numbersOfBlocks);
		for(int i=0;i<numbersOfBlocks;++i){
			scanf("%lf",&NaomiWeight[i]);
		}
		for(int i=0;i<numbersOfBlocks;++i){
			scanf("%lf",&KenWeight[i]);
		}
		std::sort(NaomiWeight,NaomiWeight+numbersOfBlocks);
		std::sort(KenWeight,KenWeight+numbersOfBlocks);
		
		printf("Case #%d: ",nowCase);
		
		answer=0;
		for(NaomiPointer=0,KenPointer=0 ; NaomiPointer<numbersOfBlocks && KenPointer<numbersOfBlocks ; \
		++KenPointer){
			while(NaomiPointer<numbersOfBlocks && NaomiWeight[NaomiPointer]<KenWeight[KenPointer]){
				++NaomiPointer;
			}
			if(NaomiPointer<numbersOfBlocks){
				++answer;
				++NaomiPointer;
			}
		}
		printf("%d ",answer);
		
		answer=0;
		for(NaomiPointer=0,KenPointer=0 ; NaomiPointer<numbersOfBlocks && KenPointer<numbersOfBlocks ; \
		++NaomiPointer){
			while(KenPointer<numbersOfBlocks && NaomiWeight[NaomiPointer]>KenWeight[KenPointer]){
				++KenPointer;
			}
			if(KenPointer<numbersOfBlocks){
				++answer;
				++KenPointer;
			}
		}
		printf("%d\n",numbersOfBlocks-answer);
		
	}
	
	return 0;
} 
