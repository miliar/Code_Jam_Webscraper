#include <iostream>
#include <fstream>

#define MAX 1000

void StandingOvation(int nTestCase);
void OpenFile(void);
void CloseFile(void);

std::ifstream fileIn;
std::ofstream fileOut;
std::string strFileInName = "A-large.in";
std::string strFileOutName = "A-large.out";

int main(void)
{	
	char strTestCase[4];
	int nTestCase = 0;

	OpenFile();
	fileIn>> strTestCase;
	nTestCase = atoi(strTestCase);

	for (int i=0; i<nTestCase; i++)
	{
		StandingOvation(i+1);
	}

	CloseFile();
	return (0);
}


void StandingOvation(int nTestCase) {
	int nTotalPeopleClapping = 0;
	int	nNeedPeopleNum = 0;
	int nSmax;
	char strDigits[MAX+2];
	char buf[1024];
	int tmpPeopleNum;
	char tmpBuf[] = "X";

	fileIn>> buf;
	nSmax = atoi(buf);

	fileIn>> strDigits;


	for (int level = 0; strDigits[level] != '\0'; level++) {		
		tmpBuf[0] = strDigits[level];
		tmpPeopleNum = atoi(tmpBuf);
		if (level > nTotalPeopleClapping) {
			int diff = level - nTotalPeopleClapping;
			nNeedPeopleNum += diff;
			nTotalPeopleClapping += diff;
		}

		nTotalPeopleClapping += tmpPeopleNum;
	}

	fileOut<< "Case #"<< nTestCase<< ": "<< nNeedPeopleNum;
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
오늘은 오페라 개막날이구 네 친구는 프리마돈나에요 ! 
너는 청중이 아닐거에요. 하지만 그녀가 열렬한 박수를 받기를 원하죠
모든 청중들이 그녀를 향해 일어서서 박수치기를요!

처음에, 모든 청중들은 앉아있어요.
청중 모두 수줍은 단계에요.
수줍음 단계인 Si의 청중들은 기다릴거에요 
적어도 Si 명의 다른 청중들이 이미 일어서서 박수를 칠때까지는요.
그리고 만일 그렇다면, 그녀는 즉시 일어서서 박수를 칠거에요.
만약 Si = 0 이면, 청중들은 즉시 항상 일어서서 박수를 칠거에요
어느 누구가 뭘하든 상관 없이요.
예를들어 Si=2인 청중은 시작시에는 앉아있을거지만,
적어도 두명의 사람이 일어서서 박수치는 걸 본 후에는 박수치기위해 일어날거에요.

너는 청중들 각각의 수줍음 단계들을 알고 있고,
끝날때 모두 일어서서 박수치는 걸 보장하는 청중이 될 프리마돈나의 친구들을 추가적으로 초대할 준비가 되어있어요.
친구들 각자는 네가 바라는 동일할 필요 없는 수줍은 수치를 갖고 있을거에요. 
네가 열렬한 박수를 보장하기위해 초대할 필요가 있는 최소 친구 수는 몇일까요?


입력

첫번째 입력 줄은 테스트 케이스 수인 T에요.
T 는 다음과 같아요.
각각은 
Smax(청중 중 가장 수줍은 사람의 최대 수줍음 단계)와 
Smax+1 자리의 문자열을 가진 한 줄로 구성되어 있습니다.
문자열의 k번째 자리(0부터 시작하여 카운트합니다)는
청중 중 얼마나 많은 사람들이 수줍음 레벨 k를 갖고 있는지를 나타냅니다.
예를들어, 문자열 "409" 는 
Si=0인 청중들이 4명, Si=2인 청중들이 9명 (그리고 Si=1은 없음 또는 다른 수치일 거에요) 을 의미할겁니다.
처음엔 항상 각 수줍음 단계를 가진 0~9명의 사람들이 있을거라는 점을 주목하세요!


출력

각 테스트 케이스에 대해,
한 줄을 출력하세요
"Case #x: y" 를 포함해서요
x는 테스트 케이스 번호 (1부터 시작) 이고 y는 네가 반드시 초대해야하는 최소 친구 수에요


제한

1 <= T <= 100

작은 자료

0 <= Smax <= 6

큰 자료

0 <= Smax <= 1000


4 (test case 4)
	
4 11111
	-> Si=0 => 1
	-> Si=1 => 1
	-> Si=2 => 1
	-> Si=3 => 1
	-> Si=4 => 1

	Case #1 : 0
		S0 은 무조건 박술 치잖아
			얘를 보고 1명이 박수를 쳐
				그럼 2명이 쳤으니까 2단계인 애가 또 쳐
					그럼 3명이 쳤으니까 3단계인 애가 또 쳐
						그럼 4명이 쳤으니까 4단계잉ㄴ 애가 또 쳐
1 09
	-> Si=0 => 0 이거나 다른 수치일 것이다.
	-> Si=1 => 9

	Si = 1
		total < need people(1)
			diff = need people - total = 1

	Case #2 : 1
	
5 110011
	-> Si=0 => 1
	-> Si=1 => 1
	-> Si=2 => 0
	-> Si=3 => 0
	-> Si=4 => 1
	-> Si=5 => 1

	최소 5명은 박수를 쳐야합니다.

	1 + 1 = 2

	Si = 4
		total < need people(4)
			diff = need people - total = 2


	만약에 두명을 추가한다면
	Si = 5
		total = 4 + 1


	Case #3 : 2
	
0 1
	Case #4 : 0

Case #1에서, 네가 인원을 추가할 필요 없이, 청중은 결국 그 자체로 일어서서 열렬한 박수를 칠거에요.
먼저 Si=0 인 청중이 일어날거에요, 그러면 Si=1인 청중이 일어날거에요 등등.

Case #2에서, Si=0인 한명의 친구는 반드시 초대되어야 합니다
하지만 전체 청중이 일어서기엔 충분해요.

Case #3에서, 최선의 해결책은 Si=2인 두명의 청중을 추가하는겁니다.

Case #4에서, 오직 한명의 청중이 있어요 그리고 그는 즉시 일어설거에요.
친구를 더 초대할 필요가 없습니다.


6 1003012

digit 1 (lv 0)
	1 (need people = 0)
	total = 1

digit 2 (lv 1)
	0 (need people = 0)
	total = 1

digit 3 (lv 2)
	0 (need people = 0)
	total = 1

digit 4 (lv 3)
	3 (need people = 3)
	total < need people
		diff = 3 - 1 = 2 명의 사람이 더 필요하다!!!

	그래서 2명을 추가했다 치고 이번 3명을 더해
	total = 3 + 3 = 6
	
digit 5 (lv 4)
	0 (need people = 0)
	total = 6

digit 6 (lv 5)
	1 (need people = 5)
	total > need people
	total = 6 + 1 = 7

digit 7 (lv 6)
	2 (need people = 6)


total 이 Si 보다 작으면 필요 친구수에 diff 만큼 추가해




*/




