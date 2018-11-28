#include <iostream>
#include <fstream>

using namespace std;

void main(){
	ifstream file; ofstream out; int t, start, end, num; 
	file.open("C-small-attempt0.in");
	out.open("out.txt");
	file >> t;                         // Определяем количество тестов
	
	for (int i = 1; i <= t; i++) {
		file >> start;
		file >> end;	                // Определяем диапазон теста
		num = 0;

		for (int j = start; j <= end; j++) {
			if ( (((int)sqrt(j) == sqrt(j)) && (j == j % 10))   ||   ((j/10 == j%10) && (sqrt(j) == j % 10))   ||   ( ((int)j/1000 == 0) && (j%10 == j/100) && ((int)sqrt(j) == sqrt(j)) && ((int)sqrt(j) % 10 == (int)sqrt(j) / 10) ) 
				|| ( ((int)j/10000 == 0) && ((int)j / 1000 == j % 10) && ((int)(j%1000)/100 == (int)(j%100)/10) && ((int)sqrt(j) == sqrt(j)) && ((int)sqrt(j) % 10 == (int)sqrt(j) / 10) )
				|| ( ((int)j/10000 != 0) && ((int)j/100000 == 0) && ((int)j / 10000 == j % 10) && (((int)j / 1000)%10 == (int)(j % 100)/10) && ((int)sqrt(j) == sqrt(j)) && ((int)sqrt(j) % 10 == (int)sqrt(j) / 100) )
				)
				num++;
		}
		out << "Case #" << i << ": " << num << endl;
	}
}