
bool checkFS(char* str)
{
	int end = strlen(str) - 1;
	int start = 0;
	
	while (start <= end)
	{
		if(str[start] != str[end]) return false;
		++start;
		--end;
	}
	return true;
}

int main(int argc, char *argv[]) {

  ifstream inputfile ("infile.txt");
  ofstream outfile ("outfile.txt");
  if (inputfile.is_open())
  {
	  int testNum;
	  inputfile >> testNum;
	  for (int i = 0; i < testNum; ++i)
	  {
		  long double to;
		  long long from;
		  int counter = 0;
		  inputfile >> from;
		  inputfile >> to;
		  long long sto = sqrt(to);
		  outfile << "Case #" << i+1 << ": ";
		  char buf[50];
		  for (long long j = 1; j <= sto; ++j)
		  {
			  char * str = itoa(j, buf, 10);
			  // check if j fair and square
			  if (checkFS(str)) {
					int j2 = j*j;
					if (j2 < from) continue;
				  	char * str2 = itoa(j2, buf, 10);
					if (checkFS(str2)) {
						++counter;
					}
			  }
		  }
		  outfile << counter << " " << endl;
	  }
  }
}