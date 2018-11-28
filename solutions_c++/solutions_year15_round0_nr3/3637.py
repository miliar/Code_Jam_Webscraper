#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <string.h>
#include <cstdlib>
#include <map>

using namespace std;

#define I (2)
#define J (3) 
#define K (4) 

int qLut[5][5] = {
  {0, 0, 0, 0, 0}, //dummy
  {0, 1, I, J, K},
  {0, I,-1, K,-J},
  {0, J,-K,-1, I},
  {0, K, J,-I,-1},
};

static int qCross(int first, int last) {
  return qLut[first][last];
}

static int qToIndex(char q) {
  if(q == 'i') return I;
  if(q == 'j') return J;
  //if(q == 'k') return K;
  return K;
}

static void test() {
  for(int i = 0; i < 5; i++) {
    for(int j = 0; j < 5; j++) {
      cout << "[" << i << "][" << j << "] = " <<  qLut[i][j] << " ";
    }
    cout << endl;
  }
}

string findK(string data, int* retFlag) {
  int flag = 1;
  int result = qToIndex(data[data.size() - 1]);
  for(int i = data.size() - 2; i >= 0; i--) {
    if(abs(result) == K) {
      if(result > 0) {
        *retFlag = 1;
      } else {
        *retFlag = -1;
      }
      return data.substr(0, i + 1);
    }

    int nextVal = qToIndex(data[i]);
    if(result < 0) {
      result = abs(result);
      flag = -1;
    } else {
      flag = 1;
    }
    result = qLut[nextVal][result] * flag;
  }
  return string("");
}


string findI(string data, int* retFlag) {
  int flag = 1;
  int result = qToIndex(data[0]);
  for(int i = 1; i < data.size(); i++) {
    if(abs(result) == I) {
      if(result > 0) {
        *retFlag = 1;
      } else {
        *retFlag = -1;
      }
      return data.substr(i);
    }

    int nextVal = qToIndex(data[i]);
    if(result < 0) {
      result = abs(result);
      flag = -1;
    } else {
      flag = 1;
    }
    result = qLut[result][nextVal] * flag;
  }
  return string("");
}

int calcStrData(string data) {
  int flag = 1;
  int result = qToIndex(data[0]);
  for(int i = 1; i < data.size(); i++) {
    //cout << "data" << i << " = " << data[i] << endl;
    int nextVal = qToIndex(data[i]);
    //cout << result << " * " << nextVal << " = " << qLut[abs(result)][nextVal] * flag << endl;
    if(result < 0) {
      result = abs(result);
      flag = -1;
    } else {
      flag = 1;
    }
    result = qLut[result][nextVal] * flag;
  }
  return result;
}
int main(int argc, char const* argv[])
{
  //test();
  std::ifstream ifs("input.txt");
  std::string str;
  if(ifs.fail()) {
    std::cerr << "can't read files " << std::endl;
    return -1;
  }
  getline(ifs, str);
  //std::cout << str << std::endl;
  
  long long probNum = 1;
  while ( getline(ifs, str))
  {
    std::stringstream ss(str);
    std::string _sLength, _repeatNum;
    int sLength, repeatNum;
    ss >> _sLength;
    ss >> _repeatNum;
    sLength = std::atoi(_sLength.c_str());
    repeatNum = std::atoi(_repeatNum.c_str());

    //cout << "sLengh:" << sLength << " repeatNum:" << repeatNum << endl;

    std::string _strData, strData;
    getline(ifs, _strData);

    strData = _strData;
    for(int i = 0; i < repeatNum - 1; i++) {
      strData += _strData;
    }

    //cout << "strData:" << strData << endl;
    //cout << calcStrData(strData) << endl;
    int retIflag = 1;
    int retKflag = 1;
    string removeI = findI(strData, &retIflag);
    //cout << "remove I:" << removeI << " flag:" << retIflag << endl;
    string removeIK = findK(removeI, &retKflag);
    //cout << "remove IK:" << removeIK << " flag:" << retIflag * retKflag << endl;
    int result = calcStrData(removeIK);
    //cout << "except IK:" << result << endl;
    //cout << "result: " << retIflag * retKflag * result << endl;
    if(retIflag * retKflag * result == J) {
      std::cout << "Case #" << probNum++ << ": YES" << std::endl;
    } else {
      std::cout << "Case #" << probNum++ << ": NO" << std::endl;
    }
  }
  return 0;
}
