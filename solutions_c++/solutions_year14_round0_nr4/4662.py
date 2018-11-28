#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cmath>

#define INPUT "A.in"
#define OUTPUT "A.out"

bool invert(int i, int j) { return (i>j); }


int main()
{

   int cases;
   double naomi[1000],ken[1000];

   freopen(INPUT,"r",stdin);
   freopen(OUTPUT,"w", stdout);

   std::cin  >> cases;

	for(int i=0;i<cases;++i)
	{
		int blocks;
		int maiorN, maiorK;
		maiorN = 0;
		maiorK = 0;

		for(int j=0;j<1000;++j)
		{
			naomi[j] = 0.000;
			ken[j] = 0.000;
		}

		std::cin >> blocks;

		for(int j=0;j<blocks;++j)
			std::cin >> naomi[j];

		for(int j=0;j<blocks;++j)
			std::cin >> ken[j];

		for(int j=0;j<blocks;++j){
			bool isMaior = false;
		 for(int k=0;k<blocks;++k){
			if(naomi[j]>ken[k])
				isMaior = true;
		 }
			if(isMaior)
			 maiorN++;

		}

		/*for(int j=0;j<blocks;++j){
			maiorK = 0;
		 for(int k=0;k<blocks;++k){
			if(ken[j]>naomi[k])
				maiorK++;
		 }
			if(maiorK==blocks)
				maiorN--;

		}

		if(maiorN<0)
			maiorN = 0;*/

		std::vector<double> vNaomi(naomi, naomi+blocks);
		std::vector<double> vKen(ken, ken+blocks);

		int cNaomi, cKen;
		cNaomi = cKen = 0;
		std::vector<double>::iterator eKen,eNaomi;

		
		std::sort(vNaomi.begin() , vNaomi.end(), std::greater<double>());
		std::sort(vKen.begin() , vKen.end());
		int count = 0;

		for(std::vector<double>::iterator it=vNaomi.begin();it!=vNaomi.end();++it)
		{
			bool existeMaior = false;
			if(cNaomi!=0||cKen!=0)
			{
			//	vNaomi.erase(eNaomi);
				vKen.erase(eKen);
			}


			for(std::vector<double>::iterator kit=vKen.begin();kit!=vKen.end();++kit)
			{
				if(*kit>*it)
				 {
					eKen = kit;
					cKen++;
					existeMaior = true;
					
				 }

			//	break;

			}	

			if(!existeMaior)
			{
				eKen = vKen.begin();
				cNaomi++;
			}

			eNaomi = vNaomi.begin()+count;
			++count;


		}


		std::vector<double> vNaomib(naomi, naomi+blocks);
		std::vector<double> vKenb(ken, ken+blocks);

		int cNaomib, cKenb;
		cNaomib = cKenb = 0;
		std::vector<double>::iterator eKenb,eNaomib;

		
		std::sort(vNaomib.begin() , vNaomib.end());
		std::sort(vKenb.begin() , vKenb.end(), std::greater<double>());
		int countb = 0;

		for(std::vector<double>::iterator it=vKenb.begin();it!=vKenb.end();++it)
		{
			bool existeMaior = false;
			if(cNaomib!=0||cKenb!=0)
			{
			//	vNaomi.erase(eNaomi);
				vNaomib.erase(eKenb);
			}


			for(std::vector<double>::iterator kit=vNaomib.begin();kit!=vNaomib.end();++kit)
			{
				if(*kit>*it)
				 {
					eKenb = kit;
					cKenb++;
					existeMaior = true;
					
				 }

			//	break;

			}	

			if(!existeMaior)
			{
				eKenb = vNaomib.begin();
				cNaomib++;
			}

			eNaomib = vKenb.begin()+count;
			++count;


		}



		std::cout << "Case #" << i+1 << ": " << blocks-cNaomib << " " << cNaomi << std::endl;
		
	



	}


   return 0;

}
