#include <iostream>
#include <fstream>

/*

	걸린 시간 = 0
	이고..

	맨 처음에는 
	[걍 모은다면 걸릴 시간]과 [농장 사는데 드는 시간] 을 비교해요.

	끝나지 않는다면.. 농장을 사겠죠.
	그럼
	걸린 시간 = 걸린 시간 + 농장 사는데 필요한 시간
	이 될거에요.
	[걍 모은다면 걸릴 시간]을 구해서 [최소 시간]에다가 넣어요.
	걍 모은다면 걸릴 시간 = 걸린 시간 + X까지 그냥 얻는 시간

	비교 대상이 필요하므로 다음 농장을 사도록 해요.
	ㄱ럼
	걸린시간 += 농장 사는데 필요한 시간
	그리고 [걍 모은다면 걸릴 시간] 을 구해서
	[최소 시간] 과 비교해요.
	만약 [걍 모은다면 걸릴 시간]이 작다면 얘를 [최소 시간]에 넣자.

	이렇게 반복하다보면..
	[최소 시간]이 [걍 모은다면 걸릴 시간] 보다 더 작은 경우가 나옵니다.
	얘를 답으로 쾅쾅쾅!
*/

#define MAX	999999

void CookieCliker(int nTestCase);
void OpenFile(void);
void CloseFile(void);

std::ifstream fileIn;
std::ofstream fileOut;
std::string strFileInName = "B-large.in";
std::string strFileOutName = "B-large.out";

int main(void)
{	
	char strTestCase[4];
	int nTestCase = 0;

	OpenFile();
	fileIn>> strTestCase;
	nTestCase = atoi(strTestCase);

	for (int i=0; i<nTestCase; i++)
	{
		CookieCliker(i+1);
	}

	CloseFile();
	return (0);
}

void CookieCliker(int nTestCase)
{
	char buf[14];	
	double nC = 0;	// 쿠키 농장 가격
	double nF = 0;	// 농장을 사면 초당 추가로 얻을 수 있는 쿠키 개수
	double nX = 0;	// 모아야 하는 쿠키 개수
	double nMinSpentTime = MAX;	// X개 까지 모으는 데에 걸리는 최소 시간
	double nNeededTimeToX = 0;	// X개 까지 모으는 데에 걸리는 시간 (소요 시간 더한거 아님)
	double nTotalSpentTime = 0;	// X개 까지 모으는 데에 걸리는 총 시간
	double nNeededTimeToBuyFarm = 0;	// 농장 사는 데에 필요한 시간
	double nNowSpentTime = 0;	// 현재까지의 소요 시간
	double nCookieProduction = 2;

	
	fileIn>> buf;
	nC = atof(buf);

	fileIn>> buf;
	nF = atof(buf);

	fileIn>> buf;
	nX = atof(buf);
	
	while (true)
	{
		nNeededTimeToX = nX / nCookieProduction;
		nTotalSpentTime = nNowSpentTime + nNeededTimeToX;
		/*
		std::cout<< "nNowSpentTime: "<< nNowSpentTime<< std::endl;
		std::cout<< "nCookieProduction: "<< nCookieProduction<< std::endl;
		std::cout<< "nNeededTimeToBuyFarm: "<< nNeededTimeToBuyFarm<< std::endl;
		std::cout<< "nNeededTimeToX: "<< nNeededTimeToX<< std::endl;
		std::cout<< "nTotalSpentTime: "<< nTotalSpentTime<< std::endl;
		std::cout<< "nMinSpentTime: "<< nMinSpentTime<< std::endl;
		std::cout<< "====================================================="<< std::endl;
		*/
		if (nTotalSpentTime < nMinSpentTime)
			nMinSpentTime = nTotalSpentTime;
		else
		{
			break;
		}

		nNeededTimeToBuyFarm = nC / nCookieProduction;
		nNowSpentTime += nNeededTimeToBuyFarm;
		nCookieProduction += nF;
	}	

	fileOut<< "Case #"<< nTestCase<< ": "<< nMinSpentTime;
	fileOut<< std::endl;
}

void OpenFile(void)
{
	fileIn.open(strFileInName);
	fileOut.open(strFileOutName);

	fileOut.precision(15);
	//std::cout.precision(15);
}

void CloseFile(void)
{
	fileIn.close();
	fileOut.close();
}



/*
	처음엔 0개의 쿠키로 시작
	초당 2개의 쿠키를 얻어요
	최소 C개의 쿠키를 갖고 있으면, 너는 쿠키 농장을 살 수 있어요
	네가 쿠키 농장을 살 때마다 너는 C개의 쿠키 만큼 지불합니다, 대신 너는 초당 추가로 F 쿠키 얻을 수 있다.

	네가 농장에 지불하지 않고 남은 X개의 쿠키를 갖고 있으면 이기는거임
	가능한한 이상적인 전략을 사용한다면, 얼마만큼의 시간이 걸려서 네가 이길것인지를 알아보자

	처음의 보유 쿠키 = 0
	C == 쿠키 농장 가격
	초당 쿠키 2개씩 증가
	농장을 사면 추가로 초당 F개씩 얻을 수 있음
	X == 보유쿠키

	C=500
	F=4.0
	X=2000.0

	best possible strategy !!
	1. 0쿠키로 시작. 초당 2개 쿠키 생산
	2. 250초 후에, c=500 쿠키를 가지게 될 것임. F=4 개 쿠키를 초당 생산하는 농장을 살 수 있음
	3. 농장을 산 후에, 0개의 쿠키가 될 것임. 그럼 너는 초당 6개의 쿠키를 생산할거야.
		사용 쿠키 = 500
		현재 걸린 시간 = 250초
		초당 6개 생산
	4. 다음 농장은 500개의 쿠키가 필요해. 그럼 넌 약 83.333333.. 초 뒤에 살 수 있지
	5. 농장을 산 후에, 너는 0개의 쿠키를 갖고, 초당 10개의 쿠키를 생산하겠지.
		사용 쿠키 = 500 + 500 = 1000
		현재 걸린 시간 = 250 + 83.3333... = 333.333333초
		초당 10개 생산
	6. 또다른 농장을 500개의 쿠키를 주고 살거야. 그럼 너는 50초 후에 살 수 있게됨.
	7. 농장을 산 후에, 너는 0개의 쿠키를 갖지. 그리고 너는 초당 14개의 쿠키를 생산함
		사용 쿠키 = 1000 + 500 = 1500
		현재 걸린 시간 = 333.333333 + 50 = 383.333333초
		초당 14개 생산
	8. 또다른 농장을 500개의 쿠키를 줘야하지만 사지 않는게 타당해. 대신 너는 2000개의 쿠키가 될 때까지 기다릴 수 있지. 아마 142.8571429초가 걸릴거야.
		만약 농장을 산다면? 
		걸릴 시간 = 383.333333 + 35.714285 = 419.047618초
		X까지 걸릴 시간은? (초당 18개 생산) 111.111111초!
		또사? 
		걸릴 시간 = 419.047618 + 27.777777 = 446.825395초
		X까지 걸릴 시간은? (초당 22개 생산) 90.9090909090초!

	총 시간 : 250 + 83.33333 + 50 + 142.8571,, = 526.198... 초!

	주목하세요!! 넌 쿠키를 지속적으로 얻을 수 있어요.
	게임이 시작한 후.. 0.1초에 0.2개의 쿠키를 얻겠지.
	게임이 시작한 후.. 파이초에 2파이개의 쿠키를 얻겠지.

	첫번째줄: 테스트 케이스
	두번째줄: 실수(C) 실수(F) 실수(X)

	(small)
	1 <= c <= 500
	1 <= f <= 4
	1 <= x <= 2000

	(large)
	1 <= c <= 10000
	1 <= f <= 100
	1 <= x <= 100000
	
	Case #x: y
	x = 테스트 케이스
	y = X개의 쿠키를 얻는 데에 걸리는 최소 시간

	
	첫번째 케이스
	C = 30.0
	F = 1.0
	X = 2.0

	1. 비교를 해보자!
	X까지 그냥 얻는 시간 = 1초
	농장 사는데 드는 시간 = 15초


	두번째 케이스
	C = 30.0
	F = 2.0
	X = 100.0

	1. 비교를 해보자!
	X까지 그냥 얻는 시간 = 50초
	농장 사는데 드는 시간 = 15초

	2. 농장을 샀어.
	보유쿠키 = 0
	초당 생산 4개.
	X까지 그냥 얻는 시간 = 25초
	농장 사는데 드는 시간 = 7.5초
	현재 걸린 시간 = 15초
	만약 걍 모은다면 총 합 = 25 + 15 = 40초!!!!

	3. 농장을 샀어
	보유쿠키 = 0
	초당 생산 6개
	X까지 그냥 얻는 시간 = 16.66666초
	농장 사는데 드는 시간 = 5초
	현재 걸린 시간 = 15 + 7.5 = 22.50초
	만약 걍 모은다면 총 합 = 22.50 + 16.666666초 = 39.166666

	4. 농장을 샀어
	보유쿠키 = 0
	초당 생산 8개
	X까지 그냥 얻는 시간 = 12.5초
	농장 사는데 드는 시간 = 3.75초
	현재 걸린 시간 = 22.5 + 5 = 27.5초
	만약 걍 모은다면 총 합 = 27.5 + 12.5 = 40

	5. 농장을 샀어
	보유쿠키 = 0
	초당 생산 10개
	X까지 그냥 얻는 시간 = 10초
	농장 사는데 드는 시간 = 3초
	현재 걸린 시간 = 27.5 + 3.75 = 31.25초
	만약 걍 모은다면 총 합 = 31.25 + 10 = 41.25초

	6. 농장을 샀어
	보유쿠키 = 0
	초당 생산 12개
	X까지 그냥 얻는 시간 = 8.333333초
	농장 사는데 드는 시간 = 2.5초
	현재 걸린 시간 = 31.25 + 3 = 34.25초
	만약 걍 모은다면 총 합 = 

	7. 농장을 샀어
	보유쿠키 = 0
	초당 생산 14개
	X까지 그냥 얻는 시간 = 7.14...초
	농장 사는데 드는 시간 = 2.1428초
	현재 걸린 시간 = 34.25 + 2.5 = 36.75초
	만약 걍 모은다면 총 합 = 

	8. 농장을 샀어
	보유쿠키 = 0
	초당 생산 16개
	X까지 그냥 얻는 시간 = 6.25초
	농장 사는데 드는 시간 = 1.875초
	현재 걸린 시간 = 
	만약 걍 모은다면 총 합 = 

*/