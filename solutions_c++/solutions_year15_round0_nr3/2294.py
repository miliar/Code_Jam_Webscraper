#include<bits/stdc++.h>

using namespace std;

const char INPUT[] = "HelloWorld.inp";
const char OUTPUT[] = "HelloWorld.out";

const int MAX_STRLEN = 10000 + 1111;

const int MAX_ORDER = 4;
const char ORDER[] = {'1', 'i', 'j', 'k'};

const int MUL_RESULT[][8] = {   {0, 1, 2, 3, 4, 5, 6, 7},
                                {1, 4, 3, 6, 5, 0, 7, 2},
                                {2, 7, 4, 1, 6, 3, 0, 5},
                                {3, 2, 5, 4, 7, 6, 1, 0},
                                {4, 5, 6, 7, 0, 1, 2, 3},
                                {5, 0, 7, 2, 1, 4, 3, 6},
                                {6, 3, 0, 5, 2, 7, 4, 1},
                                {7, 6, 1, 0, 3, 2, 5, 4}    };

int mul(int a, int b){
  return MUL_RESULT[a][b];
}

bool findDijkstra(int * str, int strLen){
  int total = 0;
  for (int idStr = 0; idStr < strLen; ++ idStr){
    total = mul(total, str[idStr]);
  }
  if (total != mul(1, mul(2, 3))){
    return false;
  }
  int prefix = 0;
  for (int idStr1 = 0; idStr1 < strLen; ++ idStr1){
    prefix = mul(prefix, str[idStr1]);
    if (prefix == 1){
      int suffix = 0;
      for (int idStr2 = strLen - 1; idStr2 > idStr1; -- idStr2){
        suffix = mul(str[idStr2], suffix);
        if (suffix == 3){
          return true;
        }
      }
    }
  }
  return false;
}

int main(void){
  freopen(INPUT, "r", stdin);
  freopen(OUTPUT, "w", stdout);

  int numTest;
  cin >> numTest;

  int str[MAX_STRLEN];
  int str2[2 * MAX_STRLEN];
  int conStart[MAX_STRLEN], conEnd[MAX_STRLEN];
  int strTimesVal[MAX_ORDER];

  for (int idTest = 0; idTest < numTest; ++ idTest){
    long long int strLen, times;
    cin >> strLen >> times;

    for (int idStr = 0; idStr < strLen; ++ idStr){
      char temp;
      cin >> temp;
      for (int idOrder = 0; idOrder < MAX_ORDER; ++ idOrder){
        if (temp == ORDER[idOrder]){
          str[idStr] = idOrder;
          break;
        }
      }
    }

    conStart[0] = str[0];
    for (int idStr = 1; idStr < strLen; ++ idStr){
      conStart[idStr] = mul(conStart[idStr - 1], str[idStr]);
    }
    conEnd[0] = str[strLen - 1];
    for (int idStr = 1; idStr < strLen; ++ idStr){
      conEnd[idStr] = mul(str[idStr], conEnd[idStr + 1]);
    }

    strTimesVal[0] = 0;
    for (int idOrder = 1; idOrder < MAX_ORDER; ++ idOrder){
      strTimesVal[idOrder] = mul(strTimesVal[idOrder - 1], conStart[strLen - 1]);
    }

    for (int idStr = 0; idStr < strLen; ++ idStr){
      str2[idStr + strLen + 2] = str2[idStr + 1] = str[idStr];
    }

    bool result = false;
    for (int idOrder1 = 0; idOrder1 < MAX_ORDER; ++ idOrder1){
      str2[0] = strTimesVal[idOrder1];
      for (int idOrder2 = 0; idOrder2 < MAX_ORDER; ++ idOrder2){
        str2[strLen + 1] = strTimesVal[idOrder2];
        for (int idStr = 0; idStr < strLen * 2 + 2; ++ idStr){

        }
        if ((times - idOrder1 - idOrder2 - 1 >= 0) && ((times - idOrder1 - idOrder2 - 1) % 4 == 0)){
          if (findDijkstra(str2, strLen + 2)){
            result = true;
            break;
          }
        }
        if (times - idOrder1 - idOrder2 - 2 >= 0){
          str2[strLen * 2 + 2] = strTimesVal[(times - idOrder1 - idOrder2 - 2) % 4];
          if (findDijkstra(str2, strLen * 2 + 3)){
            result = true;
            break;
          }
        }
      }
      if (result){
        break;
      }
    }

    /*bool result = false;
    for (int idStr1 = -1; idStr1 < strLen; ++ idStr1){
      int resultI = -1;
      for (int idOrder1 = 0; idOrder1 < MAX_ORDER; ++ idOrder1){
        if ((mul(strTimesVal[idOrder1], conStart[idStr1]) == 1) || (idStr1 == -1 && strTimesVal[idOrder1] == 1)){
          for (int idStr2 = strLen; idStr2 > idStr1; -- idStr2){
            for (int idOrder2 = 0; idOrder2 < MAX_ORDER; ++ idOrder2){
              if ((mul(conEnd[idStr2], strTimesVal[idOrder2]) == 3) || (idStr2 == strLen && strTimesVal[idOrder2] == 3)){
                //cerr << idOrder1 << " " << idOrder2 << " " << idStr1 << " " << idStr2 << endl;
                if ((times - idOrder1 - idOrder2 - 1 >= 0) && ((times - idOrder1 - idOrder2 - 1) % 4 == 0)){
                  if ((mul(conStart[idStr1], 2) == conStart[idStr2 - 1]) || (idStr1 == -1 && conStart[idStr2 - 1] == 2)){
                    //cerr << mul(conStart[idStr1], 2) << " " << conStart[idStr2 - 1] << endl;
                    result = true;
                    break;
                  }
                }
                int idOrder3 = (times - idOrder1 - idOrder2 - 2) % 4;
                if ((times - idOrder1 - idOrder2 - 2 >= 0) &&
                    (mul(conEnd[idStr1 + 1], mul(strTimesVal[idOrder3], conStart[idStr2 - 1])) == 2)){
                  //cerr << conEnd[idStr1 + 1] << " " << strTimesVal[idOrder3] << " " << conStart[idStr2 - 1] << " " << mul(strTimesVal[idOrder3], conStart[idStr2 - 1]) << endl;
                  result = true;
                  break;
                }
              }
            }
            if(result){
              break;
            }
          }
          if(result){
            break;
          }
        }
      }
      if(result){
        break;
      }
    }*/

    /*for (int idTime = 0; idTime < times; ++ idTime){
      for (int idStr = 0; idStr < strLen; ++ idStr){
        str2[idTime * strLen + idStr] = str[idStr];
      }
    }

    bool result = findDijkstra(str2, times * strLen);*/

    cout << "Case #" << (idTest + 1) << ": ";
    if (result == true){
      cout << "YES";
    } else {
      cout << "NO";
    }
    cout << endl;
  }
  return 0;
}
